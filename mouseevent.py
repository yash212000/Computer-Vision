import numpy as np
import cv2


# events = [i for i in dir(cv2) if 'EVENT' in  i]
# print(events)

def click_event(event, x, y, flags, param): #
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        # cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage=np.zeros((512,512,3),np.uint8) #creating a black image
        # print(mycolorImage.shape)
        mycolorImage[:,:]=[blue,green,red]
        print(mycolorImage[1][1])
        print(mycolorImage[12][14])
        cv2.imshow('color',mycolorImage)



# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points=[]
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
