import cv2 as cv

image = cv.imread('03_Basic_image_Drawing_Techniques/baby.jpeg')

if image is None:
    print('Image Not found')

else:
    print('Image Loaded Successfully')
    pt1 = (0, 0) # (>, v)  (Right, Down)
    pt2 = (799,799) # (<, v) (Left, Down)
    color = (100,120,140)
    thinkness = (4)

    cv.line(image, pt1, pt2, color, thinkness)
    cv.line(image, (800,0), (0,800), color, thinkness)

    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()