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
DATA
"""
image = None
win_name = "Window"

"""
CLASS DEFINITIONS
"""

"""
FUNCTIONS DEFINITIONSabsolute
"""
def mouse_handler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        cv2.circle(image, (x,y), 20, (255, 0, 0), -1)
        cv2.imshow(win_name, image)

"""
MAIN
"""
if __name__ == '__main__':
    
    # Get images
    image = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

    # Create windows
    cv2.namedWindow(win_name, cv2.WINDOW_KEEPRATIO)
    cv2.setMouseCallback(win_name, mouse_handler)

    # Display
    cv2.imshow(win_name, image)

    cv2.waitKey(0)