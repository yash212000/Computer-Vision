import cv2
import matplotlib.pyplot as plt

# matplotlib shows result in RGB format openCV in BGR format
img = cv2.imread("F:/Computer Vision/Lena.jpg")
cv2.imshow('image', img)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
