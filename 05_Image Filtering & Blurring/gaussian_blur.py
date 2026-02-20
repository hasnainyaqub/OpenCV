import cv2 as cv

image = cv.imread('03_Basic_image_Drawing_Techniques/baby.jpeg')

blurred = cv.GaussianBlur(image, (9,9), 0)

# cv.imshow('Orignal', image)
cv.imwrite('05_Image Filtering & Blurring/blurred_image.png',blurred)