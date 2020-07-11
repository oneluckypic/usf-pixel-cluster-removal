# Install Git

[Git Download](https://git-scm.com/downloads)

# Install Anaconda

[Anaconda Download](https://www.anaconda.com/products/individual)

# Install usf-mosquitos

1. Clone usf-mosquito code
```bash
git clone git@github.com:oneluckypic/usf-mosquitos.git
```

2. Activate conda base environment
```bash
conda activate base
```

# Run Script to Filter Pixel Band

Example:
```bash
python replace_band.py -b '[182,200,183,255]' -f SuisunMarsh2020_Orthomosaic_export_WedMay06033950.811478.tif
```

Print Help:
```bash
python replace_band.py --help

Usage: replace_band.py [OPTIONS]

Options:
  -f, --file PATH         Tiff image file.  [required]
  -b, --band TEXT         List of 4-channel pixels to replace, e.g. '[182, 200, 183, 255]'.  [required]
  -t, --to-band TEXT      List of 4-channel pixels to replace with.
  -r, --rng TEXT          band plus or minus range will be replaced.
  -p, --prefix TEXT       prefix to place on modified Tiff file.
  -c, --compression TEXT  Compression to use to save Tiff file. Options: raw,
                          tiff_ccitt, tiff_lzw, jpeg, tiff_adobe_deflate,
                          tiff_raw_16, packbits, tiff_thunderscan,
                          tiff_deflate, tiff_sgilog, tiff_sgilog24
  --help                  Show this message and exit.
```
