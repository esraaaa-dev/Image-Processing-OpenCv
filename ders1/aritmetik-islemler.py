import cv2
import numpy as np
image=cv2.imread('meadow.png')
#cv2.imshow('cayir',image)
#koordinatsal işlemler
print(image[80,80]) #80,80 alanı içindeki kanalların piksel degerlerini verir
image[200,200]=[255,255,255] #beyazlatma
cv2.imshow('cayir',image)
# alan=image[200:270,150:220]
# image[200:270,150:220]=alan
# image[200:270,150:220]=[255,255,255]
#cv2.imshow('cayir',image)

#rectangle
cv2.rectangle(image,(150,200),(220,270),(0,255,255),2)
#parametreler: image,koordinatlar,bgr renk(dikdörtgenin),dikdörtgenin kalınlıgı 
cv2.imshow('rectangle',image)

#toplama
x=np.uint8([250])
y=np.uint8([20])
print(x+y) #sonuc sayıların toplamının 256 ya bölümünden kalanı verir
print(cv2.add(x,y)) # sonuc sayılar toplamı 255 den büyükse 255 dir (bkz. uinit8)

logo1=cv2.imread('logo1.png')
cv2.imshow('logo1',logo1)
logo2=cv2.imread('logo2.png')
cv2.imshow('logo2',logo2)
#logoların boyutlarını shape kullanarak öğreniyoruz eger boyutları aynı olmazsa matris işlemlerini gerçekleştiremeyiz
print("logo1 in boyutu: "+str(logo1.shape))
print("logo2 nin boyutu: "+str(logo2.shape))

toplam=cv2.add(logo1,logo2)
cv2.imshow('toplama',toplam)

#agırlıklı toplama

atoplam=cv2.addWeighted(logo1,0.2,logo2,0.7,0)
cv2.imshow('agirlikli toplam',atoplam)

#cıkarma
fark=cv2.subtract(logo1,logo2)
cv2.imshow('cikarma',fark)

#carpma
carpim=cv2.multiply(logo1,logo2)
cv2.imshow('carpim',carpim)

#bölme
bölüm=cv2.divide(logo1,logo2)
cv2.imshow('bölme',bölüm)


cv2.waitKey(0)
cv2.destroyAllWindows()