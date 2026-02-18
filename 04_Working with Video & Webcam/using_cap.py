import cv2 as cv

cap =  cv.VideoCapture(0)

while True:
    ret, frame = cap.read() #return True/False and frame=image
    if not ret:
        print('could not read frame')
        break
    cv.imshow('webcam feed', frame)
     
    if cv.waitKey(1) & 0xff == ord('q'):
        print('Quitting...')
        break

cap.release()
cv.destroyAllWindows()