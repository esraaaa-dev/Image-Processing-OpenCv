import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bugday.png',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
img2=clahe.apply(img)
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

f1 = plt.figure(1)
plt.plot(hist,color='b')
plt.title('gri seviye histogram')
#plt.show()

f2 = plt.figure(2)
plt.plot(hist2,color='b')
plt.title('clahe esitleme')
plt.show()

cv2.imshow("gri seviye",img)
cv2.imshow("clahe",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#CLAHE(Contrast Limited Adaptive Histogram Equazation)
#görüntüyü parçalara ayırarak her bir kare içinde equazation yapar

