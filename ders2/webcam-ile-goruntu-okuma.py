import cv2
cap=cv2.VideoCapture(0) 
# 0 web cam için,1 usb1 için ..
# herhangi bir videodan görüntü okumak için ise videonun yolunu ya da aynı dosya içindeyse video ismini yazmak gerekir
i=0
while True:
    ret,frame=cap.read() 
    if ret == 0: #ret true/false 
        break
    i=i+1
#x,y ve her iki eksende de döndürme işlemleri
    frame2=cv2.flip(frame,1) #x ekseni
    frame3=cv2.flip(frame,0) #y ekseni
    frame4=cv2.flip(frame,-1) #x ve y eksenleri

    cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam2", frame2)
    cv2.imshow("Webcam3", frame3)
    cv2.imshow("Webcam4", frame4)

    if cv2.waitKey(1) & 0xFF== ord ('q'): # q ya basınca cık
        break 

    cap.relase()
    cv2.destroyAllWindows()