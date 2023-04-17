import cv2
import numpy
img=cv2.imread('meadow.png') #imread fonksiyonu dosyamızda bulunan fotografı okur ve okudugu bu degeri img isimli değişkene atar
img2=cv2.imread('meadow.png',0)#fotografı gri şekilde okur
cv2.imshow('cayir',img) #imshow fonksiyonu fotoğrafı ekranda gösterir
print("renkli görüntü boyutu: "+str(img.shape))
cv2.imshow('cayir2',img2)
cv2.imwrite('meadow2.png',img2)#imwrite ile yeni oluşturdugumuz gri renkli fotografı dosyamıza kaydederiz
print("gri renkli görüntü boyutu: "+str(img2.shape))

#Y satır sayısı, X sütun sayısı, Z kanal sayısı olmak üzere renkli görüntü Y x X x 3 şeklinde ifade edilir.
# Gri görüntü Y x X x 1 şeklinde ifade edilir

print(str(img.item(100,100,0))) #blue ,100*100 lük pikselde mavi degeri->211
print(str(img.item(100,100,1))) #green ,100*100 lük pikselde yeşil degeri->206
print(str(img.item(100,100,2))) #red, 100*100 lük pikselde kırmızı degeri->198
#bu üç degeri topladıgımızda 100*100lük alandaki renk tonunu buluruz

#100*100 lük alanı beyazlaştırma
img.itemset((100,100,0),255)
img.itemset((100,100,1),255)
img.itemset((100,100,2),255)
cv2.imshow('img',img)
#kanalları ayrıştırma:
#1.yol
blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
cv2.imshow('blue',blue)
cv2.imshow('green',green)
cv2.imshow('red',red)
#img[:,:,0]=255
#cv2.imshow('img',img)
#2.yol
b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)


#fotoğrafın bir kısmını kesme:
#Region of Interest(ROI)
ROI=img[170:200,200:250] #ilk bileşen y ekseni
cv2.imshow('roi',ROI)
#kestiğimiz kısmı tekrar fotografa yapıştırma
img[200:230,200:250]=ROI
cv2.imshow('eklenmis hali',img)

#fotografı yeniden boyutlandırma:
img_resize=cv2.resize(img,(500,500))
cv2.imshow('resize',img_resize)


cv2.waitKey(0)
cv2.destroyAllWindows()