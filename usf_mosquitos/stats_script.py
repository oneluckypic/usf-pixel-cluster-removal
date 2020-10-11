''' Some code from pyimagesearch'''
import click
import cv2
import numpy as np
import os

from usf_mosquitos.dataframe import dfwrite, dfread
from usf_mosquitos.imstats import kmeans_on_chip_pixels, quantile_on_kmeans, display_3d_histogram
from usf_mosquitos.imutils import rescale
from usf_mosquitos.labels import via_project_file_to_dataframe, labels_to_image_chips
from usf_mosquitos.metrics import simple_accuracy
from usf_mosquitos.replace_band import quantile_where_clause


@click.group()
def stats():
    pass


@stats.command('weeds')
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
@click.option('-o', '--out_dir', type=click.Path(), default='replace_band')
def weeds(images_dir, via_project_file, out_dir):
    label_df = via_project_file_to_dataframe(via_project_file)
    chips = labels_to_image_chips(images_dir, label_df)
    kmeans, pixels = kmeans_on_chip_pixels(chips, k=10)
    df = quantile_on_kmeans(kmeans, pixels, q=[0.15, 0.85])
    dfwrite(df, 'quant.json')
    df = dfread('quant.json')
    os.makedirs(os.path.join(images_dir, out_dir), exist_ok=True)
    metrics = []
    for file in label_df['filename'].unique():
        img = cv2.imread(os.path.join(images_dir, file))

        clause = quantile_where_clause(df, img)
        mask = np.ones((img.shape[0], img.shape[1], 1), dtype=np.uint8) * 255
        mask[clause] = 0

        # apply a series of erosions and dilations to the mask using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.erode(mask, kernel, iterations = 2)
        mask = cv2.dilate(mask, kernel, iterations = 2)
        # blur the mask to help remove noise, then apply the mask to the frame
        mask = cv2.GaussianBlur(mask, (3, 3), 0)

        metrics += [simple_accuracy(label_df[label_df['filename'] == file], mask)]
        
        img = cv2.bitwise_and(img, img, mask = np.reshape(mask, (mask.shape[0], mask.shape[1], 1)))

        cv2.imwrite(os.path.join(images_dir, out_dir, file), img)
    print('Simple Metric: ' + str(sum(metrics) / len(metrics)))


@stats.command()
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
@click.option('-c', '--class_name', type=str, help='Name of label class to display 3d histogram of')
def hist(images_dir, via_project_file, class_name):
    label_df = via_project_file_to_dataframe(via_project_file)
    chips = labels_to_image_chips(images_dir, label_df[label_df['class'] == class_name])
    display_3d_histogram(chips)


if __name__ == '__main__':
    stats()
