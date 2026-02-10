import cv2 as cv

image = cv.imread('02_Image_Transformations_and_Manipulation_Techniques/Portfolio.png', 1)

if image is not None:
    cropped = image[300:800, 500:1400]
    cv.imshow('Cropped Image', cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()