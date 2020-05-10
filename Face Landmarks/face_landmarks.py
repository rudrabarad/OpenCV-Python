import cv2                                          # importing all the packages
import numpy as np
import dlib
import os
from keras_preprocessing import image
from keras.models import model_from_json

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
# this loads the classifier to detect face

cap = cv2.VideoCapture(0)                           # this will return video from webcam

detector = dlib.get_frontal_face_detector()         # gets faces in full image but does not get in cropped image
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
# facial landmarks predictor

while True:                                         # infinite loop for keeping webcam on
    ret, frame = cap.read()                         # opens camera and read
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts to gray colour

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, face)

        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)                      # displaying the live preview of landmarks on face

    k = cv2.waitKey(1) & 0xff                       # Waits for .1(100ms) second before capturing another image
    # to increase time between each capture, increase parameters in waitKey()
    if k == 27:                                     # Press 'ESC' for exiting program
        break                                       # breaks out of the loop


# Do a bit of cleanup
cap.release()
cv2.destroyAllWindows()