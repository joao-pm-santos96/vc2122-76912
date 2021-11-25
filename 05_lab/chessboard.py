# ***********************************************************************************
# Name:           chessboard.py
# Revision:
# Date:           28-10-2019
# Author:         Paulo Dias
# Comments:       ChessBoard Tracking
#
# images         left1.jpg->left19.jpg
# Revision:
# Libraries:    Python 3.7.3 + openCV 4.1.0
# ***********************************************************************************
import numpy as np
import cv2
import glob

# Board Size
board_h = 9
board_w = 6

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Parameters
use_camera = True
do_calibration = False

def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    corner = tuple([int(corner[0]), int(corner[1])])
    
    pt0 = tuple(imgpts[0].ravel())
    pt0 = tuple([int(pt0[0]), int(pt0[1])])

    pt1 = tuple(imgpts[1].ravel())
    pt1 = tuple([int(pt1[0]), int(pt1[1])])

    pt2 = tuple(imgpts[2].ravel())
    pt2 = tuple([int(pt2[0]), int(pt2[1])])

    img = cv2.line(img, corner, pt2, (255,0,0), 5)
    img = cv2.line(img, corner, pt1, (0,255,0), 5)
    img = cv2.line(img, corner, pt0, (0,0,255), 5)
    return img

def  FindAndDisplayChessboard(img):
    # Find the chess board corners
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    # If found, display image with corners
    if ret == True:
        img = cv2.drawChessboardCorners(img, (board_w, board_h), corners, ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)

    return ret, corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Read images
images = glob.glob('.//images//left*.jpg')
img_size = None
capture = cv2 . VideoCapture(0)

if do_calibration:
    if not use_camera:
        for fname in images:
            img = cv2.imread(fname)

            if img_size is None:
                img_size = img.shape

            ret, corners = FindAndDisplayChessboard(img)
            if ret == True:
                objpoints.append(objp)
                imgpoints.append(corners)
    else:

        while ( True ) :
            ret , frame = capture.read()

            if img_size is None:
                img_size = frame.shape

            cv2.imshow ('video', frame)

            ret, corners = FindAndDisplayChessboard(frame)
            if ret == True:
                objpoints.append(objp)
                imgpoints.append(corners)
            
            if cv2.waitKey (-1) & 0xFF == ord ("q") :
                break

        

    # Compute parameters
    ret, intrinsics, distortion, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size[1::-1], None, None)

    print ( " Intrinsics : " )
    print ( intrinsics )
    print ( " Distortion : " )
    print ( distortion )

    for i in range ( len ( tvecs ) ) :
        print ( " Translations (% d ) : " % i )
        print ( tvecs[0])
        print ( " Rotation (% d ) : " % i )
        print ( rvecs[0])

    print('Saving')
    np.savez('camera.npz' , intrinsics = intrinsics , distortion = distortion)
else:
    data = np.load('camera.npz')
    intrinsics = data['intrinsics']
    distortion = data['distortion']
    
    print ( " Intrinsics : " )
    print ( intrinsics )
    print ( " Distortion : " )
    print ( distortion )



# Draw stuff
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

while ( True ) :
    ret , img = capture.read()

    if img_size is None:
        img_size = img.shape

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        
        # Find the rotation and translation vectors.
        ret,rvecs, tvecs = cv2.solvePnP(objp, corners2, intrinsics, distortion)

        for i in range ( len ( tvecs ) ) :
            print ( " Translations (% d ) : " % i )
            print ( tvecs)
            print ( " Rotation (% d ) : " % i )
            print ( rvecs)
        
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, intrinsics, distortion)

        img = draw(img,corners2,imgpts)

    cv2.imshow('img',img)

    if cv2.waitKey (5) & 0xFF == ord ("q") :
        break






capture.release()
cv2.destroyAllWindows()