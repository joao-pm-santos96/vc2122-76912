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
    h, w = image.shape

    stretched_image = cv2.equalizeHist(image)

    cv2.imshow("Equalized Image", stretched_image)
    cv2.waitKey(0)


    # Histograms
    # tuple to select colors of each channel line
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)


    # Size
    histSize = 256	 # from 0 to 255
    # Intensity Range
    histRange = [0, 256]

    fig1 = plt.figure(1)
    hist_item =  compute_histogram(image,histSize, histRange)
    plt.plot(hist_item,'r')
    plt.xlim(histRange)
    plt.title('Original Histogram')
    # fig1.show()


    fig2 = plt.figure(2)
    hist_item2 =  compute_histogram(stretched_image,histSize, histRange)
    plt.plot(hist_item2,'r')
    plt.xlim(histRange)
    plt.title('Equalized Histogram')
    
    plt.show()

    input()
