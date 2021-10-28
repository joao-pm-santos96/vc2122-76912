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

    if  np.shape(image) == ():
        # Failed Reading
        print("Image file could not be open!")
        exit(-1)

    # Display the image
    cv2.namedWindow("Original Image")
    cv2.imshow("Original Image", image)

    # Define spacing
    spacing = 20 # px

    h, w, c = image.shape
    
    # Draw horizontal lines
    for i in range(0, h, spacing):
        cv2.line(image, (0,i), (w-1,i), (0,0,0), thickness=1)

    # Draw vertical lines
    for i in range(0, w, spacing):
        cv2.line(image, (i,0), (i,h-1), (0,0,0), thickness=1)
        
    cv2.imshow("Grid Image", image)
    cv2.waitKey(0)
        # for j in range(0, spacing, w):
