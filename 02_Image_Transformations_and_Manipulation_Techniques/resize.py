import cv2 as cv

image = cv.imread('02_Image_Transformations_and_Manipulation_Techniques/Portfolio.png', 1)

if image is None:
    print('Image not found')
else:
    print('Image loaded successfully')

    resized = cv.resize(image, (500,300))
    cv.imshow('Resized Image', resized)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite('02_Image_Transformations_and_Manipulation_Techniques/Portfolio_Resize.png', resized)

    