#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import cv2
import numpy as np

from functools import partial

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
def doFloodFill(image, seed_point, win_name):

    flooded = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    diff = 5

    cv2.floodFill(flooded, mask, seed_point, 255, loDiff=5, upDiff= diff)

    cv2.imshow(win_name, flooded)

def callback(event,x,y,flags,param, image, win_name):
    if event == cv2.EVENT_LBUTTONDOWN:
        doFloodFill(image, (x, y), win_name)

def main():

    # image = cv2.imread('lena.jpg')
    image = cv2.imread('tools_2.png')
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    


    seed_point = (430, 30)
    

    # _, flooded = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    doFloodFill(image, seed_point, '2')
    
    cv2.setMouseCallback('2', partial(callback, win_name='2', image=image))
  
    cv2.imshow('1', image)
    
    cv2.waitKey(0)
    


"""
MAIN
"""
if __name__ == '__main__':
    main()