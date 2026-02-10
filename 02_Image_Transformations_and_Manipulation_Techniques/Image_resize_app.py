import cv2 as cv 

# ask user for image path
path = input('Enter image path : ')
image = cv.imread(path)

if image is None:
    print('Image not found')

else:
    print('Image loaded Successfuly')
    # ask user do you want to resize image 
    resize = input('Do you want to resize the image? (yes/no) : ')
    if resize.lower() == 'yes':
        # ask user for width and height 
        width = int(input('Enter width : '))
        height = int(input('Enter height : '))
        resized = cv.resize(image, (width, height))
        # ask user do you want to see the image or direct save.
        show_image = input('Enter do you want to see image or direct save? (yes/no)') 
        if show_image.lower() == 'yes':       
            # show the image 
            cv.imshow('Resized',resized)
            cv.waitKey(0)
            cv.destroyAllWindows()
        # Ask user do you want to save the image
        save = input('Do you want to save the image? (yes/no) : ')
        if save.lower() == 'yes':
            # ask user for path where image will save
            save_path = input('Enter the path where you want to save the image (including image name and extension : )')
            cv.imwrite(save_path, resized)