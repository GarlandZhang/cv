import cv2

import numpy as np

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  lower_red = np.array([150,10,0])
  upper_red = np.array([180,180,180])

  mask = cv2.inRange(hsv, lower_red, upper_red)
  res = cv2.bitwise_and(frame, frame, mask = mask)

  cv2.imshow('frame', frame)
  cv2.imshow('mask', mask)
  cv2.imshow('res', res)

  key = cv2.waitKey(5) & 0xFF
  if key == 27:
    break

cv2.destroyAllWindows()
cap.release()