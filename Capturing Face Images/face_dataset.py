import cv2                              # importing all the packages
import os
import numpy as np
from PIL import Image

cam = cv2.VideoCapture(0)               # to get started with videos
cam.set(3, 640)                         # set video width
cam.set(4, 480)                         # set video height

face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
# this loads the classifier to detect face

print("\n [INFO] Webcam is Opening. Please Look at the camera and wait ...")
# Initialize individual sampling face count and face_id
face_id = 1
count = 0
while (True):                                                       # infinite loop so that capturing doesn't stop
    ret, img = cam.read()                                           # opens camera and read
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    # converts to gray colour
    faces = face_detector.detectMultiScale(gray, 1.3, 5)            # detects face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # draws rectangle over face ( coordinates x,y,w,h )
        count += 1                                                  # increases face counter
        cv2.imwrite("dataset/Image " + str(face_id) + ".jpg", gray[y:y + h, x:x + w])
        # Save the captured image into the dataset folder

        face_id = face_id + 1                                       # increases face counter
        cv2.imshow('image', img)                                    # displays live window

    k = cv2.waitKey(100) & 0xff    # Waits for .1(100ms) second before capturing another image
    # to increase time between each capture, increase parameters in waitKey()
    if k == 27:                     # Press 'ESC' for exiting program
        break                       # breaks out of the loop

print("\n [INFO] Exiting Program / Cleaning Up Stuffs / Destroying Windows")
# Do a bit of cleanup

cam.release()
cv2.destroyAllWindows()