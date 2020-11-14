# Install Git

[Git Download](https://git-scm.com/downloads)

# Install Anaconda

[Anaconda Download](https://www.anaconda.com/products/individual)

# Use usf-pcr

1. Clone usf-pcr code
```bash
git clone git@github.com:oneluckypic/usf-pcr.git
```

2. Activate conda base environment
```bash
conda activate base
```

3. Print Help
```bash
python pixel_cluster_removal.py --help
```

# Purpose
This software will cluster pixel ranges together that are labeled using VGG Image Annotator (VIA). It will then remove those clustered pixel ranges from images. The pixel removal technique is based on [this blog post](https://www.pyimagesearch.com/2014/08/18/skin-detection-step-step-example-using-python-opencv/) on PyImageSearch.com. The only difference is that the pixel ranges to be removed are determined using k-means clustering of the pixels inside the labeled polygons. Images are split up into patches, with each patch analyzed individually, similarly to the how the python package [patchify](https://github.com/dovahcrow/patchify.py) works.
