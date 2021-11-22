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

    for k in [cv2.MORPH_ELLIPSE, cv2.MORPH_RECT]:
        for it in [1, 11]:

            kernel = cv2.getStructuringElement(k, (11,11))
            eroded = cv2.erode(th_inv, kernel, iterations=it)
            
            cv2.imshow('1', th)
            cv2.imshow('2', th_inv)
            cv2.imshow('3', eroded)
            cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,1))
    eroded = cv2.erode(th_inv, kernel, iterations=1)
    
    cv2.imshow('1', th)
    cv2.imshow('2', th_inv)
    cv2.imshow('4', eroded)
    cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3), anchor=(0,0))
    eroded = cv2.erode(th_inv, kernel, iterations=1)
    
    cv2.imshow('1', th)
    cv2.imshow('2', th_inv)
    cv2.imshow('5', eroded)

    cv2.imshow('diff', cv2.subtract(th_inv, eroded))
    cv2.waitKey(0)

    



"""
MAIN
"""
if __name__ == '__main__':
    main()