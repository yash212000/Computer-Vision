'''
Hough Transform Algorithm
1. Edge detection, e.g. using the Canny edge detector.
2. Mapping of edge points to the Hough space and
storage in an accumulator.
3. Interpretation of the accumulator to yield lines of
infinite length. The interpretation is done by thresholding
and possibly other constraints.
4. Conversion of infinite lines to finite lines

OpenCV implements two kind of Hough Line Transforms
-The Standard Hough Transform (HoughLines method)
-The Probabilistic Hough Line Transform (HoughLinesP method)
'''
import cv2
import numpy as np

img = cv2.imread('F://Computer Vision/sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
'''
why it was necessary to add / subtract 1000 is 
to ensure that the line was drawn over the entire image.
If the image was significantly larger the value would need to be increased proportionately.
'''

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()