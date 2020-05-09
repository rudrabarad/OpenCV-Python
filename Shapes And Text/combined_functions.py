import numpy as np
import cv2

background = np.zeros((600, 500, 4), dtype='uint8')

cv2.rectangle(background, (80, 50), (430, 405), (225, 225, 225), 1)

cv2.circle(background, (255, 220), 130, (0, 0, 225), 20)

cv2.line(background, (255, 220), (255, 305), (0, 0, 225), 20)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(background, "POWER", (65, 540), font, 3.5, (0, 0, 255), 3, cv2.LINE_8)

cv2.imshow('combined-functions', background)

cv2.waitKey(0)
cv2.destroyAllWindows()
