 # Aula_01_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Paulo Dias - 09/2021



#import
import numpy as np
import cv2
import sys

# Read the image
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED )
threshold = int(sys.argv[2]) 


if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics
height, width = image.shape

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % (image.dtype))

# Crete copy
image2 = image.copy()

# Threshold copy
for x in range(width-1):
	for y in range(height-1):
		image2[x,y] = 0 if image2[x,y]<threshold else image2[x,y]


# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )
cv2.namedWindow( "Modified window", cv2.WINDOW_AUTOSIZE )

# Show the image
cv2.imshow( "Display window", image )
cv2.imshow( "Modified window", image2 )

# Wait
cv2.waitKey( 0 )

# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
