import cv2
import numpy as np

cap = cv2.VideoCapture('walkers.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while cap.isOpened():
  actual_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
  diff = cv2.absdiff(frame1, frame2)
  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)

  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
  dilated = cv2.dilate(thresh, None, iterations=3)

  contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour) >= 2000:
      face_candid = actual_gray[x:x+w,y:y+h]
      faces = face_cascade.detectMultiScale(face_candid, 1.3, 5)
      cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
      for (x, y, w, h) in faces:
         cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
         cv2.putText(frame1, "Face detection: {}".format('Face here'), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
      # cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

  #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

  # cv2.imshow('data', dilated)
  cv2.imshow('feed', frame1)

  frame1 = frame2
  ret, frame2 = cap.read()

  if cv2.waitKey(40) == 27:
    break



cv2.destroyAllWindows()
cap.release()