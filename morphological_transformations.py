import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('smarties.png', 0)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)  # converting image into binary

kernal = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)  # increases the corners/boundary
erosion = cv2.erode(mask, kernal, iterations=1)  # decreases/corrodes the boundary
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)  # erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)  # dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)  # difference between dilation and erosion of image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)  # difference between image and opening
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]
for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
