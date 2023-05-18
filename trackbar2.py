# import numpy as np
import cv2


def nothing(x):
    pass  # print(x)


# img = cv2.imread('lena.jpg')   doubt: why are we putting this in infinite loop,why we need to read again and again?

cv2.namedWindow('image')

cv2.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while True:
    img = cv2.imread('lena.jpg')
    pos = cv2.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))
    if cv2.waitKey(1) == ord('a'):
        break

    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)

cv2.destroyAllWindows()
