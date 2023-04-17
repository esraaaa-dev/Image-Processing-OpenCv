import cv2
import numpy as np

def func(x):
    pass

cv2.namedWindow("Trackbar")

cv2.resizeWindow("Trackbar",500,250)

cv2.createTrackbar("Lower-H","Trackbar",0,180,func)
cv2.createTrackbar("Lower-S","Trackbar",0,255,func)
cv2.createTrackbar("Lower-V","Trackbar",0,255,func)

cv2.createTrackbar("Upper-H","Trackbar",0,180,func)
cv2.createTrackbar("Upper-S","Trackbar",0,255,func)
cv2.createTrackbar("Upper-V","Trackbar",0,255,func)

cv2.setTrackbarPos("Upper-H","Trackbar",180)
cv2.setTrackbarPos("Upper-S","Trackbar",255)
cv2.setTrackbarPos("Upper-V","Trackbar",255)

frame = cv2.imread("meadow.png")

while 1:

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("Lower-H","Trackbar")
    ls = cv2.getTrackbarPos("Lower-S","Trackbar")
    lv = cv2.getTrackbarPos("Lower-V","Trackbar")

    uh = cv2.getTrackbarPos("Upper-H","Trackbar")
    us = cv2.getTrackbarPos("Upper-S","Trackbar")
    uv = cv2.getTrackbarPos("Upper-V","Trackbar")

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lower_color,upper_color)
    bitwise = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("original",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#vid.relase()
cv2.destroyAllWindows()