
import os

import cv2
import pandas as pd
import yaml


def to_row(image, region):
    shape = region['shape_attributes']
    attrs = region['region_attributes']
    return [image['filename'], attrs['class'], shape['y'], shape['x'], shape['width'], shape['height']]


def via_dict_to_dataframe(via_dict):
    md = via_dict['_via_img_metadata']
    data = [to_row(image, region) for image in md.values() for region in image['regions']]
    return pd.DataFrame(data, columns=['filename', 'class', 'row', 'col', 'width', 'height'])


def via_project_file_to_dataframe(via_proj_file):
    with open(via_proj_file, 'r') as file:
        return via_dict_to_dataframe(yaml.safe_load(file))


def chip_image(img, boxes_df):
    return [img[box.row:box.row+box.height, box.col:box.col+box.width] for index, box in boxes_df.iterrows()]


def labels_to_images(images_dir, df):
    images = [cv2.imread(os.path.join(images_dir, file)) for file in df['filename'].unique()]
    return list(zip(df['filename'].unique(), images))


def labels_to_image_chips(images, df):
    ''' Use box labels to extract image chips.
    Args:
        images_dir: location of image files
        df: labels dataframe
    '''
    df = df[df['class'] != 'Background']
    chips = []
    for filename, image in images:
        labels = df[df['filename'] == filename]
        chips += chip_image(image, labels)
    return chips
