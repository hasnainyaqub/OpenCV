import cv2 as cv

image = cv.imread('02_Image_Transformations_and_Manipulation_Techniques/baby.jpeg', 1)

if image is not None:
    image = cv.resize(image, (500, 300))

    horizontal_flip = cv.flip(image, 1)
    vertical_flip = cv.flip(image, 0)
    both_flip = cv.flip(image, -1)

    cv.imshow('Original Image', image)
    cv.imshow('Horizontal Flip', horizontal_flip)
    cv.imshow('vertical Flip', vertical_flip)
    cv.imshow('Both Flip',both_flip)

    cv.waitKey(0)
    cv.destroyAllWindows()