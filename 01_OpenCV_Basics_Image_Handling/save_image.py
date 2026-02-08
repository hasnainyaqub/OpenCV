import cv2
# Load an image from file
image = cv2.imread('01_OpenCV_Basics_Image_Handling/Portfolio_SS.png', 0)
if image is not None:
    # Save the image to a new file
    success = cv2.imwrite('01_OpenCV_Basics_Image_Handling/Portfolio_Gray.png', image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error saving image.")
else:    print("Error loading image.")