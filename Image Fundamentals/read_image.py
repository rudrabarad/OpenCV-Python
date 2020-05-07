import numpy as np      # used to handle all the multi dimensional arrays within the picture
import cv2

img = cv2.imread('scene_jpg.jpg', 1)     # used to read an colourful image
cv2.imshow('Original', img)              # to display image
cv2.waitKey(0)
cv2.destroyAllWindows()
