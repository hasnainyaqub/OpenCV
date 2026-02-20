import cv2 as cv

image = cv.imread('05_Image Filtering & Blurring/blur_image.png')

blurred = cv.medianBlur(image, 11)

cv.imwrite('05_Image Filtering & Blurring/median_blurred_image2.png',blurred)