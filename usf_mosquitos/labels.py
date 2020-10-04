
import pandas as pd
import yaml


def to_data(image, region):
    shape = region['shape_attributes']
    return [image['filename'], shape['x'], shape['y'], shape['width'], shape['height']]


def via_dict_to_dataframe(via_dict):
    md = via_dict['_via_img_metadata']
    data = [to_data(image, region) for image in md.values() for region in image['regions']]
    return pd.DataFrame(data, columns=['filename', 'x', 'y', 'width', 'height'])


def via_project_file_to_dataframe(via_proj_file):
    with open(via_proj_file, 'r') as file:
        return via_json_to_dataframe(yaml.safe_load(file))
