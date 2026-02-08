import cv2 

image = cv2.imread('01_OpenCV_Basics_Image_Handling/Portfolio_SS.png', 1)

if image is not None:
    print("Image loaded successfully.")
    print("Image shape:", image.shape)
    print("Image data type:", image.dtype)
    cv2.imshow('Image', image) # Display the image in a window
    cv2.waitKey(0) # Wait for a key press to close the window
    cv2.destroyAllWindows() # Close the window after displaying the image
else:
    print("Error: Image not found.")