import cv2 as cv

image = cv.imread('03_Basic_image_Drawing_Techniques/baby.jpeg')

if image is None:
    print('Image Not found')

else:
    print('Image Loaded Successfully')
    
    center = (240,240)

    cv.circle(
    image, # image
    center, # center
    120 , # Redius
    (0, 0, 255), # color
    2 # thickness
    )
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()