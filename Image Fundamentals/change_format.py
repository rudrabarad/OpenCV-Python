import numpy as np      # used to handle all the multi dimensional arrays within the picture
import cv2

img = cv2.imread('scene_jpg.jpg', 0)     # used to read an grey image
img = cv2.imwrite('PNG Format/scene_png.png', img)   # to save image in png format with grey color in subfolder
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# running this code will save grey image in png format in same folder
