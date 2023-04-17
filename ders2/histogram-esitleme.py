import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bugday.png',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
equ = cv2.equalizeHist(img)
hist2 = cv2.calcHist([equ],[0],None,[256],[0,256])

f1 = plt.figure(1)
plt.plot(hist,color='b')
plt.title('gri seviye histogram')
#plt.show()

f2 = plt.figure(2)
plt.plot(hist2,color='b')
plt.title('gri seviye histogram esitleme')
plt.show()

cv2.imshow("gri seviye",img)
cv2.imshow("histogram_esitleme",equ)

cv2.waitKey(0)
cv2.destroyAllWindows()

#histogram esitleme renkleri düzgün dagılmamıs görüntülerin renklerini esitler