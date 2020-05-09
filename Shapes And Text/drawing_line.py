import numpy as np
import cv2

background = np.zeros((500, 500, 4), dtype='uint8')
# to create a black background .zeros((pt1,pt1,channels), dtype='8-bit signed integer')

cv2.line(background, (250, 250), (450, 450), (225, 225, 225), 1, lineType=8, shift=0)
# .line(pic,pt1,pt2,color,thickness.line-type,shift(decrease) )

cv2.imshow('line', background)
# .image(name of window, object to show)

cv2.waitKey(0)
cv2.destroyAllWindows()
