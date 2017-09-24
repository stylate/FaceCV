#!usr/bin/env python3.6
import cv2, sys
# from image import * // clean both codes later

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# sets video source to webcam
video_capture = cv2.VideoCapture(0)

# video is now captured, frame-by-frame.
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, 
            minNeighbors = 5, minSize = (30, 30), 
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w), (y + h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)
    
    # user quits by pressing 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
