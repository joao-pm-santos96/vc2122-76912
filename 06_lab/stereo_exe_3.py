#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
import numpy as np
import cv2
import glob
from functools import partial

"""
METADATA
"""
__author__ = 'Joao Santos'
__copyright__ = 'Copyright December2021'
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
def mouse_handler(event, x, y, flags, params, F, right_image = None, left_image = None):
    if event == cv2.EVENT_LBUTTONDOWN:
        p = np.asarray([x,y])

        which_image = 2 if right_image is not None else 1 if left_image is not None else None


        epilineR = cv2.computeCorrespondEpilines(p.reshape(-1,1,2), which_image, F)
        epilineR = epilineR.reshape(-1, 3)[0]

        color = np.random.randint(0, 255, 3).tolist()
        x0 = int(0)
        y0 = int((-epilineR[2] - x0 * epilineR[0]) / epilineR[1])

        x1 = int(1000)
        y1 = int((-epilineR[2] - x1 * epilineR[0]) / epilineR[1])

        if left_image is not None:
            cv2.line(left_image, (x0, y0), (x1, y1), color, thickness=4)
            cv2.imshow(left_window, left_image)

        if right_image is not None:
            cv2.line(right_image, (x0, y0), (x1, y1), color, thickness=4)
            cv2.imshow(right_window, right_image)

"""
MAIN
"""
# Board Size
board_h = 9
board_w = 6

left_window = 'Left Undist'
right_window = 'Right Undist'

if __name__ == '__main__':
    
    stereo_params = np.load('stereoParams.npz')
    images_right = sorted(glob.glob('.//images//right*.jpg'))
    images_left = sorted(glob.glob('.//images//left*.jpg'))

    right_undist = cv2.undistort(cv2.imread(images_right[0]), stereo_params['intrinsics1'], stereo_params['distortion1'])

    left_undist = cv2.undistort(cv2.imread(images_left[0]), stereo_params['intrinsics2'], stereo_params['distortion2'])

    # cv2.imshow('Right Original', cv2.imread(images_right[0]))
    # cv2.imshow('Left Original', cv2.imread(images_left[0]))

    cv2.imshow(right_window, right_undist)
    cv2.setMouseCallback('Right Undist', partial(mouse_handler, F=stereo_params['F'], left_image = left_undist))
    
    cv2.imshow(left_window, left_undist)
    cv2.setMouseCallback('Left Undist', partial(mouse_handler, F=stereo_params['F'], right_image = right_undist))

    
    cv2.waitKey(0)

    