import cv2


cam = cv2.VideoCapture(0)

# cam2 = cv2.VideoCapture(1)

while True: 

     ignore, frame = cam.read()
    # ignore, frame = cam2.read()
    grayFilter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('my webcam', frame)
    cv2.imshow('my webcam2', grayFilter)
    cv2.imshow('my webcam3', grayFilter)
    cv2.imshow('my webcam4', frame)



    cv2.moveWindow('my webcam', 0, 0)
    cv2.moveWindow('my webcam2', 1000, 0)
    cv2.moveWindow('my webcam3', 0, 500)
    cv2.moveWindow('my webcam4', 1000, 500)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()