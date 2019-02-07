from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2

def contrast(image):
    contr = cv2.convertScaleAbs(image, alpha=0.5, beta=1) #contrast if alfa<beta
    cv2.imwrite("contr.jpg", contr)
    cv2.imshow('Contrast', contr)

def brigtness(image):
    bright = cv2.convertScaleAbs(image, alpha=3.0, beta=0) #brigtness if alfa>beta
    cv2.imwrite("bright.jpg", bright)
    cv2.imshow('Brightness', bright)

url = tkfd.askopenfilename()
image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)
brigtness(image_rgb)
contrast(image_rgb)
cv2.waitKey(0)