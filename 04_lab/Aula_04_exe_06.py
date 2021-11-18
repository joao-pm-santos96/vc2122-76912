#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import cv2

"""
METADATA
"""
__author__ = 'Joao Santos'
__copyright__ = 'Copyright November2021'
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
def main():

    image = cv2.imread('art4.bmp')

    for size in [23, 5, 51]:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size,size))
        closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        
        cv2.imshow('1', image)
        cv2.imshow('2', closing)
        cv2.waitKey(0)

    


"""
MAIN
"""
if __name__ == '__main__':
    main()