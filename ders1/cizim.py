import cv2
import numpy as np

img=cv2.imread('meadow.png')

#dikdörtgen
cv2.rectangle(img,(50,100),(100,150),(0,0,255),2)
cv2.imshow('dikdortgen',img)

#cizgi 
print(img.shape) #->(230,328,3)
cv2.line(img,(0,0),(230,328),(255,0,0),2)
cv2.imshow('line',img)
cv2.line(img,(100,150),(150,200),(0,255,255),3)
cv2.imshow('line',img)

#daire
cv2.circle(img,(60,60),25,(0,0,255),2)
cv2.imshow('daire',img)

#yazı ekleme

cv2.putText(img,'cayir',(60,60),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,111,120),4,cv2.LINE_4)
cv2.imshow('text',img)




cv2.waitKey(0)
cv2.destroyAllWindows()