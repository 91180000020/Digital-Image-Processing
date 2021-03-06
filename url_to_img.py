from skimage import io
import tkinter as tk
from tkinter import filedialog as tkfd
import numpy as np
import cv2

url = tkfd.askopenfilename()

image = io.imread(url)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Original", image_rgb)
cv2.waitKey(0)