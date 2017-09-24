#!/usr/bin/env python3.6

import cv2

imagePath = sys.argv[1]
cascPath = sys.argv[2]

# haar cascade is made.
faceCascade = cv2.CascadeClassifier(cascPath)

# read image and convert it to grayscale.
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# face detection in cascade
'''
# detectMultiScale is a function that detects objects.
# scaleFactor compensates for objects in the back that are seen to be smaller
# than those in the front.
minNeighbors := how many objects are detected near current object before
                it declares whether or not the face is found.
minSize := size of each window.
'''
faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5,
            minSize = (30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

# Draw rectangle around face.
# (x, y) denotes the rectangle's location, and (w, h) denotes its width and height.
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)
