"""
Bitwise operations
1, image combine
2, Cut out
3, Flip / Remove

1- cv.bitwise_and(image1, image2) # AND
2- cv.bitwise_or(image1, image2) # OR
3- cv.bitwise_not(image1) # NOT

* img1 img2 height widh same
** use only black and white
*** 
"""

import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)

cv.circle(img1,(150,150), 100, 255, -1)
cv.rectangle(img2,(100,100), (250,250), 255, -1)

bitwise_and = cv.bitwise_and(img1, img2)
bitwise_or = cv.bitwise_or(img1, img2)
bitwise_not = cv.bitwise_not(img1)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('bitwise_and', bitwise_and)
cv.imshow('bitwise_or', bitwise_or)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()