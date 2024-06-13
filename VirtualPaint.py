import cv2
import numpy as np
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

myColors = [[133,56,0,159,156,255]]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]),mask)

while True:
    success, img = cap.read()
    findColor(img,myColors)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break