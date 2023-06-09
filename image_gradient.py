import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('sudoku.png', 0)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelcombined=cv2.bitwise_or(sobelX,sobelY)

titles = ['Original Image', 'Laplacian', 'SobelX', 'SobelY','Sobel Combined']
images = [img, lap, sobelX, sobelY,sobelcombined]
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
