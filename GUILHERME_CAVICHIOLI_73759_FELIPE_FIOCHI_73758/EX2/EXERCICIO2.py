import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("coins.png", 0)

cv2.imshow("coins", img)
