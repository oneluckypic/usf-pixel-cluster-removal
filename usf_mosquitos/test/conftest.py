
import pandas as pd
import pytest


@pytest.fixture
def via_proj():
    via_proj = {"_via_img_metadata": 
                   {"2e89c04f374dc64e1a37f02d0849144d.jpg8336637":
                       {"filename": "2e89c04f374dc64e1a37f02d0849144d.jpg",
                        "size": 8336637,
                        "regions": [{"shape_attributes":
                                        {"name": "rect",
                                         "x":1792,
                                         "y":328,
                                         "width":40,
                                         "height":50},
                                     "region_attributes":{}},
                                    {"shape_attributes":
                                        {"name": "rect",
                                         "x":2296,
                                         "y":444,
                                         "width":42,
                                         "height":50},
                                     "region_attributes":{}}],
                        "file_attributes":{}},
                    "4ec7caecb917cfb520e58423ca228e63.jpg9018387":
                        {"filename": "4ec7caecb917cfb520e58423ca228e63.jpg",
                         "size": 9018387,
                         "regions": [{"shape_attributes":
                                         {"name": "rect",
                                          "x":2551,
                                          "y":297,
                                          "width":65,
                                          "height":41},
                                      "region_attributes":{}},
                                     {"shape_attributes":
                                         {"name": "rect",
                                          "x":1534,
                                          "y":437,
                                          "width":41,
                                          "height":39},
                                      "region_attributes":{}}],
                         "file_attributes": {}}}}
    return via_proj


@pytest.fixture
def via_dataframe():
    columns = ['filename', 'x', 'y', 'width', 'height']
    data = [['2e89c04f374dc64e1a37f02d0849144d.jpg', 1792, 328, 40, 50],
             ['2e89c04f374dc64e1a37f02d0849144d.jpg', 2296, 444, 42, 50],
             ['4ec7caecb917cfb520e58423ca228e63.jpg', 2551, 297, 65, 41],
             ['4ec7caecb917cfb520e58423ca228e63.jpg', 1534, 437, 41, 39]]
    return pd.DataFrame(data, columns=columns)
