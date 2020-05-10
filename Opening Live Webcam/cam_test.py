import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # turning on webcam
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while (True):    # infinite loop for live webcam
    ret, frame = cap.read()     # for reading the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting image to grey

    cv2.imshow('frame', frame)  # displaying the image continuously to show live video

    k = cv2.waitKey(100) & 0xff  # Waits for .1(100ms) second before capturing another image
    # to increase time between each capture, increase parameters in waitKey()
    if k == 27:  # Press 'ESC' for exiting program
        break  # breaks out of the loop

cap.release()
cv2.destroyAllWindows()