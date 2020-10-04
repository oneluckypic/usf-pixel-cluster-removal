
import click

from usf_mosquitos.histogram import labels_to_hist
from usf_mosquitos.labels import via_project_file_to_dataframe

@click.command()
@click.option('-d', '--images_dir', type=click.Path(), help='Directory containing images')
@click.option('-p', '--via_project_file', type=click.Path(), help='Path to VIA project file')
def click_hist(images_dir, via_project_file):
    df = via_project_file_to_dataframe(via_project_file)
    labels_to_hist(images_dir, df)


if __name__ == '__main__':
    click_hist()
