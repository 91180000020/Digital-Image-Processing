from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2

def erosion(image):
    erosion_img = cv2.erode(image, kernel, iterations=1)
    cv2.imwrite('erosion_img.jpg', erosion_img)
    cv2.imshow("Erosion", erosion_img)

def dilation(image):
    dilation_img = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite('dilation_img.jpg', dilation_img)
    cv2.imshow("Dilation", dilation_img)

def opening(image):
    open_img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('open_img.jpg', open_img)
    cv2.imshow("Openning Image", open_img)

def closing(image):
    close_img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('close_img.jpg', close_img)
    cv2.imshow("Closing Image", close_img)

def morph_gradient(image):
     gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
     cv2.imwrite('gradient_img.jpg', gradient)
     cv2.imshow("Gradient Image", gradient)


url = tkfd.askopenfilename()
image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)
kernel = np.ones((5, 5), np.uint8)

erosion(image_rgb)
dilation(image_rgb)
opening(image_rgb)
closing(image_rgb)
morph_gradient(image_rgb)
cv2.waitKey(0)