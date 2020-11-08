# Install Git

[Git Download](https://git-scm.com/downloads)

# Install Anaconda

[Anaconda Download](https://www.anaconda.com/products/individual)

# Use usf-weeds

1. Clone usf-weeds code
```bash
git clone git@github.com:oneluckypic/usf-weeds.git
```

2. Activate conda base environment
```bash
conda activate base
```

3. Print Help
```bash
python stats_script.py --help
```

# Purpose
This is a script to remove certain types of weeds from imagery. The weeds must be labeled in imagery first using VGG Image Annotator (VIA). See labels directory. Then the algorithm will try to characterize the weed pixels using k-means clustering. The weed pixels will be removed using a series of erosion and dilation convolutions on the images.

# Hyperparameter Search Results (Top 4 after search 4200 combinations)

| K  | Quantile   | Erosion Kernel | Dilation Kernel | Gaussian Blur Kernel | Score              |
| -- | ---------- | -------------- | --------------- | -------------------- | ------------------ |
| 15 | [0.1, 0.9] | (3, 3)         | (11, 11)        | (7, 7)               | 0.7382699128181481 |
| 15 | [0.1, 0.9] | (3, 3)         | (11, 11)        | (11, 11)             | 0.7308652994827931 |
| 15 | [0.1, 0.9] | (3, 3)         | (11, 11)        | (3, 3)               | 0.7291169219729912 |
| 15 | [0.1, 0.9] | (3, 3)         | (11, 11)        | (5, 5)               | 0.7287373520837732 |
