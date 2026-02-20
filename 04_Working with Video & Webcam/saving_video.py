import cv2 as cv 

camera = cv.VideoCapture(0)

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('04_Working with Video & Webcam/output.mp4', codec, 25, (frame_width, frame_height))

while True:
    success, frame = camera.read()
    
    if not success:
        break

    output.write(frame)
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xff == ord('q'):
        print('Quitting...')
        break
camera.release()
output.release()