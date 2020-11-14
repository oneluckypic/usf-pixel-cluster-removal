''' This script is a simple replacement of pixel values.  Given a pixel band and
    range this script will find pixels that fall with in the band's range and replace
    them with another pixel 4-channel set of values (by default black).
    
    python replace_band.py --help
'''
import click
import json
import numpy as np
import os
from PIL import Image

compressions = ["raw", "tiff_ccitt", "tiff_lzw", "jpeg",
                "tiff_adobe_deflate", "tiff_raw_16",  "packbits", "tiff_thunderscan",
                "tiff_deflate", "tiff_sgilog", "tiff_sgilog24"]

@click.command()
@click.option('-f', '--file', type=click.Path(), required=True, help='Tiff image file.')
@click.option('-b', '--band', required=True,
              help='List of 4-channel pixels to replace, e.g. \'[182, 200, 183, 255]\'.')
@click.option('-t', '--to-band', default='[0, 0, 0, 0]',
              help='List of 4-channel pixels to replace with.')
@click.option('-r', '--rng', default='[30, 30, 30, 30]',
              help='band plus or minus range will be replaced.')
@click.option('-p', '--prefix', default='mod_', help='prefix to place on modified Tiff file.')
@click.option('-c', '--compression', default='tiff_lzw',
              help='Compression to use to save Tiff file. Options: ' + ', '.join(compressions))
def replace_band(file, band, to_band, rng, prefix, compression):
    band = json.loads(band)
    to_band = json.loads(to_band)
    rng = json.loads(rng)
    
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(file)
    imarray = np.array(im)
    w = np.where((band[0] - rng[0] < imarray[:, :, 0]) & (imarray[:, :, 0] < band[0] + rng[0]) &
                 (band[1] - rng[1] < imarray[:, :, 1]) & (imarray[:, :, 1] < band[1] + rng[1]) &
                 (band[2] - rng[2] < imarray[:, :, 2]) & (imarray[:, :, 2] < band[2] + rng[2]) &
                 (band[3] - rng[3] < imarray[:, :, 3]) & (imarray[:, :, 3] < band[3] + rng[3]))
    imarray[w] = to_band
    im = Image.fromarray(imarray)
    to_file = os.path.join(os.path.dirname(file), prefix + os.path.basename(file))
    im.save(to_file, compression=compression)


def quantile_where_clause(quant_df, img):
    clause = False
    for i, df in quant_df.groupby('cluster'):
        df = df.sort_values(by='quantile').reset_index()
        blue = np.logical_and(df['b'][0] < img[:, :, 0], img[:, :, 0] < df['b'][1])
        green = np.logical_and(df['g'][0] < img[:, :, 1], img[:, :, 1] < df['g'][1])
        red = np.logical_and(df['r'][0] < img[:, :, 2], img[:, :, 2] < df['r'][1])
        bgr_clause = np.logical_and(blue, np.logical_and(green, red))
        clause = np.logical_or(clause, bgr_clause)
    return clause


if __name__ == '__main__':
    replace_band()
