import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cars.xml')
# face_cascade = cv2.CascadeClassifier('images/classifier/cascade.xml')

# img = cv2.imread('face_from_vid.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x, y, w, h) in faces:
#   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('cars.avi')

while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 5)
  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)

  cv2.imshow('img', img)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()