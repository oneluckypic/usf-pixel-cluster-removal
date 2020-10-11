
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def kmeans_on_chip_pixels(chips, k=5):
    pixels = [np.squeeze(np.reshape(chip, (1, chip.shape[0] * chip.shape[1], 3))) for chip in chips]
    pixels = np.concatenate(pixels)
    kmeans = KMeans(n_clusters=k).fit(pixels)
    return kmeans, pixels


def quantile_on_kmeans(kmeans, pixels, q=[0.25, 0.75]):
    df = pd.DataFrame(np.column_stack((kmeans.labels_, pixels)), columns=['cluster', 'b', 'g', 'r'])
    return df.groupby('cluster').quantile(q=q).reset_index().rename(columns={'level_1': 'quantile'})


def display_3d_histogram(images, size=5000, bins=8):
    
    hist = cv2.calcHist(images, [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    
    print("3D histogram shape: %s, with %d values" % (
    hist.shape, hist.flatten().shape[0]))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ratio = size / np.max(hist)
    
    for (x, plane) in enumerate(hist):
        for (y, row) in enumerate(plane):
            for (z, col) in enumerate(row):
                if hist[x][y][z] > 0.0:
                    siz = ratio * hist[x][y][z]
                    rgb = (z / (bins - 1), y / (bins - 1), x / (bins -1))
                    ax.scatter(x, y, z, s = siz, facecolors = rgb)

    plt.show()
