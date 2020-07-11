# Install Git

(Git Download)[https://git-scm.com/downloads]

# Install Anaconda

(Anaconda Download)[https://www.anaconda.com/products/individual]

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
```
