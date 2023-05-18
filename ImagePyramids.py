'''
Pyramid, or pyramid
representation, is a type of
multi-scale signal
representation in which a signal
or an image is subject to
repeated smoothing and
subsampling.
Two types of image pyramids in openCV
1. Gaussian pyramid
2. Laplacian pyramid

They help in blending and reconstruction of image.

We dont have seperate function for laplacian pyramid , it is formed using gaussian pyramid
A level in Laplacian Pyramid
is formed by the difference
between that level in
Gaussian Pyramid and
expanded version of its
upper level in Gaussian
Pyramid.
'''

import cv2
# import numpy as np

img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    #cv2.imshow(str(i), layer)

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()






# img = cv2.imread('lena.jpg')
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# hr2 = cv2.pyrUp(lr1)
#
# cv2.imshow('original image', img)
# cv2.imshow("pyrDown 1 image", lr1)
# cv2.imshow("pyrDown 2 image", lr2)
# cv2.imshow("pyrUp 1 image", hr2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
