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

    img_size = image.shape
    h = img_size[0]
    w = img_size[1]

    if (len(img_size) > 2):
        color = (127,127,127)
    else:
        color = (255,255,255)
    
    # Draw horizontal lines
    for i in range(0, h, spacing):
        cv2.line(image, (0,i), (w-1,i), color, thickness=1)

    # Draw vertical lines
    for i in range(0, w, spacing):
        cv2.line(image, (i,0), (i,h-1), color, thickness=1)
        
    cv2.imshow("Grid Image", image)
    cv2.waitKey(0)
    cv2.imwrite('grid_image.png', image)
