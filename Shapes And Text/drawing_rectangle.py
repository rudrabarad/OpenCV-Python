import numpy as np
import cv2

background = np.zeros((600, 600, 3), dtype='uint8')
# to create a black background .zeros((pt1,pt1,channels), dtype='8-bit signed integer')

cv2.rectangle(background, (100, 100), (500, 500), (225, 225, 225), 1, lineType=8, shift=0)
# .rectangle(pic,pt2,pt2,color,thickness.line-type,shift(decrease))

cv2.imshow('rectangle', background)
# .image(name of window, object to show)


cv2.waitKey(0)
cv2.destroyAllWindows()
