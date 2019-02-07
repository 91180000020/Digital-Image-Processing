from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2

def crop(image):
    cropped = image[70:170, 440:540]
    cv2.imwrite("cropped.png", cropped)
    cv2.imshow("cropped", cropped)

def resize_cubic(image):
    cubic_img = cv2.resize(image, None, 2, 2, cv2.INTER_CUBIC)
    cv2.imwrite("cubic.jpg", cubic_img)
    cv2.imshow("Resized Cubic", cubic_img)

def resize_area(image):
    area_img = cv2.resize(image, None, 2, 2, cv2.INTER_AREA)
    cv2.imwrite("area.jpg", area_img)
    cv2.imshow("Resized Area", area_img)

def resize_linear(image):
    linear_img = cv2.resize(image, None, 2, 2, cv2.INTER_LINEAR)
    cv2.imwrite("linear.jpg", linear_img)
    cv2.imshow("Resized Linear", linear_img)

def translation(image):
    (rows, cols) = image.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    trans = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite("transformed.jpg", trans)
    cv2.imshow("Transformed", trans)

def rotation(image):
    (rows, cols) = image.shape[:2]
    M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    rot = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite("rotated.jpg", rot)
    cv2.imshow("Rotated", rot)

def affine_transform(image):
    (rows, cols, ch) = image.shape[:3]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    affine = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite("affine.jpg", affine)
    cv2.imshow("Affine", affine)

def perspective_transform(image):
    (rows, cols, ch) = image.shape[:3]
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    perspect = cv2.warpPerspective(image, M, (300, 300))
    cv2.imwrite("perspective.jpg", perspect)
    cv2.imshow("Perspective", perspect)


url = tkfd.askopenfilename()
image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)
resize_cubic(image_rgb)
resize_area(image_rgb)
resize_linear(image_rgb)
translation(image_rgb)
rotation(image_rgb)
affine_transform(image_rgb)
perspective_transform(image_rgb)
crop(image_rgb)
cv2.waitKey(0)