import cv2 as cv

image = cv.imread('03_Basic_image_Drawing_Techniques/baby.jpeg')

if image is None:
    print('Image Not found')

else:
    print('Image Loaded Successfully')
    w , h = image.shape[:2]

    cv.putText(image, 'Hello! I am a Programmer', (w//3,h//2), 
               cv.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,300), 5 )
    
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()