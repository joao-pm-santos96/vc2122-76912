# ***********************************************************************************
# Name:           chessboard.py
# Revision:
# Date:           28-10-2019
# Author:         Paulo Dias
# Comments:       ChessBoard Tracking
#
# images         left1.jpg->left19.jpg
# Revision:
# ***********************************************************************************
import numpy as np
import cv2
import glob

# Board Size
board_h = 9
board_w = 6

def  FindAndDisplayChessboard(img):
    # Find the chess board corners
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    # If found, display image with corners
    if ret == True:
        img = cv2.drawChessboardCorners(img, (board_w, board_h), corners, ret)
        cv2.imshow('img',img)
        cv2.waitKey(100)

    return ret, corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
obj_points = [] # 3d point in real world space
left_corners = []
right_corners = []

img_size = None

# Read images
images = sorted(glob.glob('..//images//left*.jpg'))

for fname in images:
    img = cv2.imread(fname)

    if img_size is None:
        img_size = img.shape

    ret, corners = FindAndDisplayChessboard(img)
    if ret == True:
        obj_points.append(objp)
        left_corners.append(corners)

images = sorted(glob.glob('..//images//right*.jpg'))

for fname in images:
    img = cv2.imread(fname)
    ret, corners = FindAndDisplayChessboard(img)
    if ret == True:
        # objpoints.append(objp)
        right_corners.append(corners)


# print('Right corners')
# print(right_corners)

# print('Left corners')
# print(left_corners)

# print('Object points')
# print(obj_points)

# Stereo calibration
ret, cam_matrix_right, dist_coeffs_right, cam_matrix_left, dist_coeffs_left, R, T, E, F = cv2.stereoCalibrate(obj_points, right_corners, left_corners, None, None, None, None, img_size[1::-1], flags=cv2.CALIB_SAME_FOCAL_LENGTH)

print(cam_matrix_right)
print(cam_matrix_left)

np.savez('stereoParams.npz',
    intrinsics1=cam_matrix_right,
    distortion1=dist_coeffs_right,
    intrinsics2=cam_matrix_left,
    distortion2=dist_coeffs_left,
    R=R,
    T=T,
    E=E,
    F=F)





cv2.waitKey(-1)
cv2.destroyAllWindows()