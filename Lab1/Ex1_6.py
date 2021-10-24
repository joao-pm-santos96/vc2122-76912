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
FUNCTIONS DEFINITIONS
"""

"""
MAIN
"""
if __name__ == '__main__':
    
    image = None
    win_name = "Window"

    # Get images
    image = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

    # Convert
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create windows
    cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)

    # Display
    cv2.imshow(win_name, image)

    cv2.waitKey(0)

    cv2.imshow(win_name, image_gray)

    cv2.waitKey(0)