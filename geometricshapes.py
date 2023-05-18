import cv2

img = cv2.imread("F:/Computer Vision/Lena.jpg", 1)  # 1 for colored, 0 for grayscale ,-1 for unchanged(oroginal image)

img = cv2.line(img, (255, 255), (512, 512), (255, 0, 0), 2)
img = cv2.arrowedLine(img, (0, 255), (500, 500), (255, 255, 0), 2)
cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1) #if we put -1 in last argument then color fills in whole space.
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Lena Paul', (10, 500), font, 3, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(img.shape)
