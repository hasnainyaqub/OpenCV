import cv2

image = cv2.imread('01_OpenCV_Basics_Image_Handling/Portfolio_SS.png', 1)

if image is not None:
    h, w, c = image.shape
    print(f'Height Pixels: {h}\nWidth Pixels: {w}\nColor Channels: {c}')
    print(f"Image dimensions: {h}x{w} pixels with {c} color channels.")
else:
    print("Error loading image.")