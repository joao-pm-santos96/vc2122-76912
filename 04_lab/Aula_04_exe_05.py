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

    image = cv2.imread('art3.bmp')

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    
    cv2.imshow('1', image)
    cv2.imshow('2', opening)
    cv2.waitKey(0)

    image = cv2.imread('art2.bmp')

    for size in [(3,9), (9,3)]:

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        
        cv2.imshow('1', image)
        cv2.imshow('2', opening)
        cv2.waitKey(0)


"""
MAIN
"""
if __name__ == '__main__':
    main()