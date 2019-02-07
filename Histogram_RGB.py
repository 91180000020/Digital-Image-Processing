from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2
from matplotlib import pyplot as plt

def show_color_histogram(image):
    for i, col in enumerate(['b', 'g', 'r']):
        draw_image_histogram(image, [i], color=col)
    plt.show()

def draw_image_histogram(image, channels, color='k'):
    hist = cv2.calcHist([image], channels, None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

url = tkfd.askopenfilename()

image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", image_rgb)

img_to_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_rgb = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('hist_equ_rgb.jpg', hist_equalization_rgb)
cv2.imshow("Hist Result RGB", hist_equalization_rgb)
show_color_histogram(image)
#cv2.imshow('result.jpg')
cv2.waitKey(0)
