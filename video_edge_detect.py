import cv2
import numpy as np

cap = cv2.VideoCapture('maroon5.avi')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    gauss_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    gray_hist1 = cv2.equalizeHist(gray, 1)
    cv2.imshow('frame', gray)
    cv2.imshow('Edge Detected with Canny', edges)
    cv2.imshow('Filtered with Gaussian Blur', gauss_blur)
    cv2.imshow('Histogram Equalised', gray_hist1)
    cv2.waitKey(25)

cap.release()
cv2.destroyAllWindows()

