import cv2 as cv
import numpy as np

image = cv.imread('05_Image Filtering & Blurring/blur_img.png')

sharpen_kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])

sharpened = cv.filter2D(image, -1, sharpen_kernel)

# cv.imwrite('05_Image Filtering & Blurring/sharpened_image.png',sharpened)

cv.imshow('Original', image)
cv.imshow('Sharpened', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()