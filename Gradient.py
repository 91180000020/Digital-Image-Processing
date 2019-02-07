from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2

def laplacian_gradient(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    cv2.imwrite('laplacian_img.jpg', laplacian)
    cv2.imshow("Laplacian", laplacian)

def sobelX_gradient(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    cv2.imwrite('sobelX_img.jpg', sobelx)
    cv2.imshow("Sobel according to X", sobelx)

def sobelY_gradient(image):
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imwrite('sobelY_img.jpg', sobely)
    cv2.imshow("Sobel according to y", sobely)


url = tkfd.askopenfilename()
image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)

laplacian_gradient(image_rgb)
sobelX_gradient(image_rgb)
sobelY_gradient(image_rgb)
cv2.waitKey(0)