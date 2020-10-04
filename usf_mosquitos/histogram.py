'''
Some histogram code from PyImageSearch
Practical Python and OpenCV, 4th Edition
Chapter 7
'''
import cv2
from matplotlib import pyplot as plt

import os

from usf_mosquitos.labels import labels_to_chips

def labels_to_hist(images_dir, df):

    chips = labels_to_chips(images_dir, df)
    channels = [cv2.split(chip) for chip in chips]
        
    colors = ('b', 'g', 'r')
       
    plt.figure()
    plt.title("’Flattened’ Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for channel, color in zip(zip(*channels), colors):
        hist = cv2.calcHist(list(channel), [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
    
