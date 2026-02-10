import cv2 as cv

# ask user for image path
image_path = input("Enter the path to the image: ")
# read the image
image = cv.imread(image_path)
if image is not None:
    print("Image loaded successfully.")
    #ask user to display the image
    display = input("Do you want to display the image? (yes/no): ")
    if display.lower() == 'yes':
        cv.imshow('Image', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    # ask user to save the image?
    save = input("Do you want to save the image? (yes/no): ")
    if save.lower() == 'yes':
        #ask user for normal or grayscale
        grayscale = input("Do you want to save the image in grayscale? (yes/no): ")
        if grayscale.lower() == 'yes':
            gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            save_path = input("Enter the path to save the grayscale image (including filename and extension): ")
            cv.imwrite(save_path, gray_image)
            print(f"Grayscale image saved at: {save_path}")
        else:
            save_path = input("Enter the path to save the image (including filename and extension): ")
            cv.imwrite(save_path, image)
            print(f"Image saved at: {save_path}")

else:
    print("Error loading image. Please check the path and try again.")