import cv2
import numpy as np
from matplotlib import pyplot as plt

#Lendo a imagem
img = cv2.imread("lena.jpg")

#Aplicando filtro blur
blur = cv2.GaussianBlur(img, (15,15),0)

subtrair = cv2.subtract(img,blur)

filtroWeighted = cv2.addWeighted(img, 0.1, blur, 1, 0)

cv2.imshow("LenaOriginal", img)
cv2.imshow("LenaEditada", filtroWeighted)
