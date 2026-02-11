import cv2 as cv

path = input("Enter image path : ")
image = cv.imread(path)

if image is None:
    print('Image not found')

else:
    print('Image loaded successfully')

    user = int(input('What you want to do with image. 1. Draw line, 2. Draw Rectangle, 3. Draw Text, 4. Draw Circle (1/2/3/4) : '))

    if user == 1:
        # Take tuple inputs
        pt1 = tuple(map(int, input("Enter first point x,y : ").split(',')))
        pt2 = tuple(map(int, input("Enter second point x,y : ").split(',')))
        color = tuple(map(int, input("Enter color r,g,b : ").split(',')))
        thickness = int(input("Enter thickness : "))
        
        cv.line(image, pt1, pt2, color, thickness)
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif user == 2:
        pt1 = tuple(map(int, input("Enter first point x,y : ").split(',')))
        pt2 = tuple(map(int, input("Enter second point x,y : ").split(',')))
        color = tuple(map(int, input("Enter color r,g,b : ").split(',')))
        thickness = int(input("Enter thickness : "))
        
        cv.rectangle(image, pt1, pt2, color, thickness)
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif user == 3:
        text = input("Enter text, you want to add in image : ")
        center = tuple(map(int, input("Enter center point x,y : ").split(',')))
        redius = int(input("Enter redius : "))
        color = tuple(map(int, input("Enter color r,g,b : ").split(',')))
        thickness = int(input("Enter thickness : "))
        
        cv.putText(image, text, center, 
                   cv.FONT_HERSHEY_SIMPLEX, redius, color, thickness )
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    elif user == 4:
        center = tuple(map(int, input("Enter center point x,y : ").split(',')))
        redius = int(input("Enter redius : "))
        color = tuple(map(int, input("Enter color r,g,b : ").split(',')))
        thickness = int(input("Enter thickness : "))
        
        cv.circle(image, center, redius, color, thickness)
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print('choose from 1 to 4')