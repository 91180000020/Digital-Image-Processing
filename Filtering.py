from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2


def filtering2D(image):
    kernel = np.ones((3, 3), np.float32) / 25
    dst = cv2.filter2D(image, -1, kernel)
    cv2.imwrite('filter2D.jpg', dst)
    cv2.imshow("2D Filter", dst)


def filtering_boxFilter(image):
    blur = cv2.blur(image, (3, 3))
    cv2.imwrite('box_filter.jpg', blur)
    cv2.imshow("Box Filter(Blur)", blur)


def filtering_gaussianBlur(image):
    gauss_blur = cv2.GaussianBlur(image, (3, 3), 0)
    cv2.imwrite('gaussian_blur_filter.jpg', gauss_blur)
    cv2.imshow("Gaussian Blur Filter", gauss_blur)


def filtering_meianBlur(image):
    median_blur = cv2.medianBlur(image, 3)
    cv2.imwrite('median_blur_filter.jpg', median_blur)
    cv2.imshow("Median Blur Filter", median_blur)


def filtering_biteral(image):
    biteral = cv2.bilateralFilter(image, 15, 75, 75)
    cv2.imwrite('biteral_filter.jpg', biteral)
    cv2.imshow("Biteral Filter", biteral)


url = tkfd.askopenfilename()
image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)

filtering2D(image_rgb)
filtering_boxFilter(image_rgb)
filtering_gaussianBlur(image_rgb)
filtering_meianBlur(image_rgb)
filtering_biteral(image_rgb)
cv2.waitKey(0)
