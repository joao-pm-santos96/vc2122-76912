#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

"""
METADATA
"""
__author__ = 'Joao Santos'
__copyright__ = 'Copyright October2021'
__credits__ = ['Joao Santos']
__version__ = '1.0.0'
__maintainer__ = 'Joao Santos'
__email__ = 'joao.pm.santos96@gmail.com'
__status__ = 'Production'
# __license__ = 'GPL'

"""
TODO
"""

"""
CLASS DEFINITIONS
"""

"""
FUNCTIONS DEFINITIONS
"""
def compute_histogram(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

"""
MAIN
"""
if __name__ == '__main__':
    
    # Read the image from argv
    image = cv2.imread(sys.argv[1] , cv2.IMREAD_UNCHANGED)
    stretched_image = image.copy()

    if  np.shape(image) == ():
        # Failed Reading
        print("Image file could not be open!")
        exit(-1)

    # Display the image
    cv2.namedWindow("Original Image")
    cv2.namedWindow("Stretched Image")

    cv2.imshow("Original Image", image)

    # Get size
    h, w, c = image.shape

    for ch in range(c):
        # Get min and max values
        min_val,max_val,min_indx,max_indx=cv2.minMaxLoc(image[:,:,ch])

        for i in range(h):
            for j in range(w):
                # print(str(i) + ' ' + str(j))
                # print(image[i,j,ch])
                stretched_image[i,j,ch] = ((image[i,j,ch] - min_val) / (max_val - min_val)) * 255

    cv2.imshow("Stretched Image", stretched_image)
    cv2.waitKey(1)


    # Histograms
    # tuple to select colors of each channel line
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)

    # create the histogram plot, with three lines, one for
    # each color
    fig1 = plt.figure(1)
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.title("Original Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    fig1.show()

    fig2 = plt.figure(2)
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        stretched_histogram, bin_edges = np.histogram(
            stretched_image[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], stretched_histogram, color=c)

    plt.title("Stretched Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    fig2.show()

    input()










    exit(0)
    # Compute histograms
    # Size
    histSize = 256	 # from 0 to 255
    # Intensity Range
    histRange = [0, 256]
    original_hist = compute_histogram(image,histSize,histRange)

    one = plt.figure(1)
    plt.plot(original_hist,'r')
    plt.title("Original Histogram")
    plt.xlim(histRange)
    one.show()

    stretch_hist = compute_histogram(stretched_image,histSize,histRange)

    two = plt.figure(2)
    plt.plot(stretch_hist,'r')
    plt.title("Stretch Histogram")
    plt.xlim(histRange)
    two.show()

    input()





    