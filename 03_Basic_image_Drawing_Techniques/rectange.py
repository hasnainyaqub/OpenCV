import cv2 as cv

image = cv.imread('03_Basic_image_Drawing_Techniques/baby.jpeg')

if image is None:
    print('Image Not found')

else:
    print('Image Loaded Successfully')

    cv.rectangle(image, (40,50), (500,500), (0,0,255), 5)
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
