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

    b,g,r = cv2.split(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('rgb', image)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)

    # Color histogram
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])

    plt.figure(2)
    histr = cv2.calcHist([gray],[0],None,[256],[0,256])
    plt.plot(histr,color = 'b')
    plt.xlim([0,256])
    
    plt.show()

    