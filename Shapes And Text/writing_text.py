import numpy as np
import cv2

background = np.zeros((500, 500, 4), dtype='uint8')
# to create a black background .zeros((pt1,pt1,channels), dtype='8-bit signed integer')

font = cv2.FONT_HERSHEY_DUPLEX
# define the font

cv2.putText(background, "RUDRA", (50, 200), font, 4, (255, 255, 255), 3, cv2.LINE_8)
cv2.putText(background, "BARAD", (50, 330), font, 4, (255, 255, 255), 3, cv2.LINE_8)

# .circle(img,text,pts,font,size,color,thickness,type of line)

cv2.imshow('text', background)
# .image(name of window, object to show)

cv2.waitKey(0)
cv2.destroyAllWindows()
