
import os

import cv2
import pandas as pd
import yaml


def to_row(image, region):
    shape = region['shape_attributes']
    return [image['filename'], shape['y'], shape['x'], shape['width'], shape['height']]


def via_dict_to_dataframe(via_dict):
    md = via_dict['_via_img_metadata']
    data = [to_row(image, region) for image in md.values() for region in image['regions']]
    return pd.DataFrame(data, columns=['filename', 'row', 'col', 'width', 'height'])


def via_project_file_to_dataframe(via_proj_file):
    with open(via_proj_file, 'r') as file:
        return via_dict_to_dataframe(yaml.safe_load(file))


def labels_to_chips(images_dir, df):
    ''' Use box labels to extract image chips.
    Args:
        images_dir: location of image files
        df: labels dataframe
    '''
    chips = []
    for filename, boxes in df.groupby('filename'):
        img = cv2.imread(os.path.join(images_dir, filename))
        chips += [img[box.row:box.row+box.height, box.col:box.col+box.width] for index, box in boxes.iterrows()]
    return chips
