import numpy as np      # used to handle all the multi dimensional arrays within the picture
import cv2

img = cv2.imread('scene_jpg.jpg', 0)     # used to read an grey image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

