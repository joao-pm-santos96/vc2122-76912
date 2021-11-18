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

    image = cv2.imread('wdg2.bmp')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 120, 256, cv2.THRESH_BINARY)

    th_inv = cv2.bitwise_not(th)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    dilated = cv2.dilate(th_inv, kernel, iterations=1)

    edges = cv2.subtract(dilated, th_inv)
    
    cv2.imshow('1', th)
    cv2.imshow('2', th_inv)
    cv2.imshow('3', dilated)
    cv2.imshow('4', edges)
    cv2.waitKey(0)

    



"""
MAIN
"""
if __name__ == '__main__':
    main()