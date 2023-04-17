import cv2
import numpy as np
import requests

url="http://192.168.1.9:8080//shot.jpg"
i=0
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    frame = cv2.resize(img, (640, 480))
    i=i+1
    cv2.putText(img=frame, text='Frame'+str(i), org=(25, 80), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(0, 255, 0),thickness=2)
   

    cv2.imshow("Android Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
