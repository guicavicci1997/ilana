import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", 0)

cv2.imshow("lena", img)
