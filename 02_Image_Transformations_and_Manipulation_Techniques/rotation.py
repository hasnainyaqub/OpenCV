import cv2 as cv

image = cv.imread('02_Image_Transformations_and_Manipulation_Techniques/Portfolio.png', 1)

if image is None:
    print('Image not found')

else:
    image = cv.resize(image, (500, 300))
    (h,w)= image.shape[:2]
    center = (w//2, h//2)

    M = cv.getRotationMatrix2D(center, 60, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))

    cv.imshow('Original Image', image)
    cv.imshow('Rotated Image', rotated)

    cv.waitKey(0)
    cv.destroyAllWindows()
