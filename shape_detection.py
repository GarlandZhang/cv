import numpy as np
import cv2

img = cv2.imread('shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
  approx = cv2.approxPolyDP(contour, 0.000001 * cv2.arcLength(contour, True), True)
  cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
  x = approx.ravel()[0]
  y = approx.ravel()[1]
  if len(approx) == 3:
    # ****gave up here because tutorial is just based on shapes

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()