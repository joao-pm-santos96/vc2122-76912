#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import numpy as np
import cv2
import sys

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
FUNCTIONS DEFINITIONSabsolute
"""

"""
MAIN
"""
if __name__ == '__main__':
    
    # Get images
    image1 = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
    image2 = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED)

    # Subtract using both methods
    sub_cv = cv2.subtract(image1, image2)
    sub_np = np.subtract(image1, image2)

    # Create windows
    cv2.namedWindow("OpenCV subtraction", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("numpy subtraction", cv2.WINDOW_AUTOSIZE)

    # Display
    cv2.imshow("OpenCV subtraction", sub_cv)
    cv2.imshow("numpy subtraction", sub_np)

    cv2.waitKey(0)