''' Some code from pyimagesearch'''
import click
import cv2
import itertools
import numpy as np
import os
import random

from usf_mosquitos.dataframe import dfwrite, dfread
from usf_mosquitos.imstats import kmeans_on_chip_pixels, quantile_on_kmeans, display_3d_histogram
from usf_mosquitos.imutils import rescale
from usf_mosquitos.labels import via_project_file_to_dataframe, labels_to_image_chips
from usf_mosquitos.metrics import simple_accuracy
from usf_mosquitos.replace_band import quantile_where_clause


@click.group()
def stats():
    pass


@stats.command('hyper')
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
@click.option('-o', '--out_dir', type=click.Path(), default='replace_band')
def weeds(images_dir, via_project_file, out_dir):

    kernels = [(3, 3), (5, 5), (7, 7)]

    k = [5, 10, 15]
    q = [[0.10, 0.90], [0.25, 0.75], [0.4, 0.6]]
    erosion = kernels
    dilation = kernels
    blur = kernels

    parameters = list(itertools.product(k, q, erosion, dilation, blur))
    random.shuffle(parameters)
    for p in parameters:
        accuracy = algorithm(images_dir, via_project_file, out_dir, k=p[0], q=p[1],
                            erosion_kernel=p[2], dilation_kernel=p[3], blur_kernel=p[4])
        print(str(p) + ', ' + str(accuracy))


@stats.command('weeds')
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
@click.option('-o', '--out_dir', type=click.Path(), default='replace_band')
def weeds(images_dir, via_project_file, out_dir):
    algorithm(images_dir, via_project_file, out_dir)


def algorithm(images_dir, via_project_file, out_dir,
              k=10, q=[0.15, 0.85],
              erosion_kernel=(5, 5), dilation_kernel=(5, 5), blur_kernel=(3, 3)):
    label_df = via_project_file_to_dataframe(via_project_file)
    chips = labels_to_image_chips(images_dir, label_df)
    kmeans, pixels = kmeans_on_chip_pixels(chips, k=k)
    df = quantile_on_kmeans(kmeans, pixels, q=q)
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
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, erosion_kernel)
        mask = cv2.erode(mask, kernel, iterations = 2)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, dilation_kernel)
        mask = cv2.dilate(mask, kernel, iterations = 2)
        # blur the mask to help remove noise, then apply the mask to the frame
        mask = cv2.GaussianBlur(mask, blur_kernel, 0)

        metrics += [simple_accuracy(label_df[label_df['filename'] == file], mask)]
        
        img = cv2.bitwise_and(img, img, mask = np.reshape(mask, (mask.shape[0], mask.shape[1], 1)))

        cv2.imwrite(os.path.join(images_dir, out_dir, file), img)
    return sum(metrics) / len(metrics)


@stats.command('hist')
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
@click.option('-c', '--class_name', type=str, help='Name of label class to display 3d histogram of')
def hist(images_dir, via_project_file, class_name):
    label_df = via_project_file_to_dataframe(via_project_file)
    chips = labels_to_image_chips(images_dir, label_df[label_df['class'] == class_name])
    display_3d_histogram(chips)


@stats.command('via')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
def via(via_project_file):

    import json
    import pytest
    import yaml
    
    with open(via_project_file, 'r') as file:
        via_dict = yaml.safe_load(file)

    md = via_dict['_via_img_metadata']
    for image in md.values():
        for region in image['regions']:
            region['region_attributes']['class'] = 'Lepidium'

    with open(via_project_file, 'w') as file:
        json.dump(via_dict, file, indent=4, sort_keys=True)


if __name__ == '__main__':
    stats()
