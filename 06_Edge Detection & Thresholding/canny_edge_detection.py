import cv2 as cv

image = cv.imread('05_Image Filtering & Blurring/baby.jpeg', cv.IMREAD_GRAYSCALE)

ret, thresh_img = cv.threshold(image, 120,255, cv.THRESH_BINARY)

edges = cv.Canny(image, 100, 200)

cv.imshow('Original', image)
cv.imshow('Edges', thresh_img)
cv.waitKey(0)  
cv.destroyAllWindows()

"""
90 - 0 Black
130 - 255 white
180 - 255 white
50 - 0 black

100,120,150
best
"""