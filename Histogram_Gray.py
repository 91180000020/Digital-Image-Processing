from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2
from matplotlib import pyplot as plt


def show_grayscale_histogram(image):
    draw_image_histogram(image, [0])
    plt.show()


def draw_image_histogram(image, channels, color='k'):
    hist = cv2.calcHist([image], channels, None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])


url = tkfd.askopenfilename()

image = io.imread(url)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

gray_hist0 = cv2.equalizeHist(gray, 0)
gray_hist1 = cv2.equalizeHist(gray, 1)
gray_hist2 = cv2.equalizeHist(gray, 2)
cv2.imwrite('hist_equ_gray0.jpg', gray_hist0)
cv2.imwrite('hist_equ_gray1.jpg', gray_hist1)
cv2.imwrite('hist_equ_gray2.jpg', gray_hist2)
cv2.imshow("Hist Result Gray0", gray_hist0)
cv2.imshow("Hist Result Gray1", gray_hist1)
cv2.imshow("Hist Result Gray2", gray_hist2)
show_grayscale_histogram(gray)
cv2.waitKey(0)
