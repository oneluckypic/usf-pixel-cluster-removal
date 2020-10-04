
from usf_mosquitos.labels import via_project_file_to_dataframe
from usf_mosquitos.histogram import labels_to_hist

def test_labels_to_hist():
    via_proj_file = '/Users/daric/dev/git/usf-mosquitos/labels/lepidium/via_project_lepidium_simple.json'
    images_dir = '/Users/daric/dev/data/USF_Jessie_Daric/'
    df = via_project_file_to_dataframe(via_proj_file)
    labels_to_hist(images_dir, df)
