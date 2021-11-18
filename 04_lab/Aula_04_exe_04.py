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

    image = cv2.imread('mon1.bmp')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 90, 256, cv2.THRESH_BINARY)

    th_inv = cv2.bitwise_not(th)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    eroded = cv2.erode(th_inv, kernel, iterations=2)
    
    cv2.imshow('1', th)
    cv2.imshow('2', th_inv)
    cv2.imshow('3', eroded)
    cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    eroded = cv2.erode(th_inv, kernel, iterations=2)
    
    cv2.imshow('1', th)
    cv2.imshow('2', th_inv)
    cv2.imshow('3', eroded)
    cv2.waitKey(0)

"""
MAIN
"""
if __name__ == '__main__':
    main()