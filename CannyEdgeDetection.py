'''
The Canny edge detector is an edge detection operator
that uses a multi-stage algorithm to detect a wide range
of edges in images. It was developed by John F. Canny
in 1986.
The Canny edge detection algorithm is
composed of 5 steps:
1. Noise reduction
2. Gradient calculation
3. Non-maximum suppression
4. Double threshold
5. Edge Tracking by Hysteresis
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('messi5.jpg', 0)
canny = cv2.Canny(img, 100, 200)

titles = ['Original Image', 'Canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
