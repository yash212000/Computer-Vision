import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Halftone_Gaussian_Blur.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

titles = ['Original Image', '2D Convolution']
images = [img, dst]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
'''
LPF helps in removing noises,
blurring the images.
HPF filters helps in finding edges in
the images.
'''
'''Median filter is something that replace
each pixel's value with the median of its
neighboring pixels. This method is great
when dealing with "salt and pepper
noise". '''

'''When you need to preserve the edges then use bilateral filter'''


