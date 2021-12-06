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
            # cv2.imshow(left_window, left_image)

        if right_image is not None:
            cv2.line(right_image, (x0, y0), (x1, y1), color, thickness=4)
            # cv2.imshow(right_window, right_image)

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

    # get image size
    img_size = cv2.imread(images_left[0]).shape

    R1 = np.zeros(shape=(3,3))
    R2 = np.zeros(shape=(3,3))
    P1 = np.zeros(shape=(3,4))
    P2 = np.zeros(shape=(3,4))
    Q = np.zeros(shape=(4,4))

    intrinsics1 = stereo_params['intrinsics1']
    distortion1 = stereo_params['distortion1']
    intrinsics2 = stereo_params['intrinsics2']
    distortion2 = stereo_params['distortion2']

    cv2.stereoRectify(intrinsics1,
    distortion1,
    intrinsics2,
    distortion2,
    img_size[1::-1], 
    stereo_params['R'],
    stereo_params['T'],
    R1,
    R2,
    P1,
    P2,
    Q,
    flags=cv2.CALIB_ZERO_DISPARITY,
    alpha=-1,
    newImageSize=(0,0))

    # Map computation
    print('Init rectify map')
    map1_x, map1_y = cv2.initUndistortRectifyMap(intrinsics1, 
        distortion1,
        R1,
        P1,
        img_size[1::-1],
        cv2.CV_32FC1)

    map2_x, map2_y = cv2.initUndistortRectifyMap(intrinsics2, 
        distortion2,
        R2,
        P2,
        img_size[1::-1],
        cv2.CV_32FC1)

    right_undist =  cv2.remap(cv2.imread(images_right[0]), map1_x, map1_y, cv2.INTER_LINEAR)

    left_undist =  cv2.remap(cv2.imread(images_left[0]), map2_x, map2_y, cv2.INTER_LINEAR)

    cv2.namedWindow(right_window)
    cv2.setMouseCallback(right_window, partial(mouse_handler, F=stereo_params['F'], left_image = left_undist))

    cv2.namedWindow(left_window)
    cv2.setMouseCallback(left_window, partial(mouse_handler, F=stereo_params['F'], right_image = right_undist))

    while True:

        cv2.imshow(right_window, right_undist)
        cv2.imshow(left_window, left_undist)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break





