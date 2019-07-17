import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
  ret, frame = cap.read()
  blur = cv2.GaussianBlur(frame, (15,15), 0)
  fgmask = fgbg.apply(blur)

  kernel = np.ones((15, 15), np.float32) / 225
  smoothed = cv2.filter2D(fgmask, -1, kernel)

  cv2.imshow('original', frame)
  cv2.imshow('fg', fgmask)

  k = cv2.waitKey(30) & 0xFF
  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()