import cv2 as cv 

camera = cv.VideoCapture(0)

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('04_Working with Video & Webcam/output.mp4', codec, 20.0, (frame_width, frame_height))

while True:
    ret, frame = camera.read()
    if not ret:
        print('Could not read frame')
        break
    output.write(frame)