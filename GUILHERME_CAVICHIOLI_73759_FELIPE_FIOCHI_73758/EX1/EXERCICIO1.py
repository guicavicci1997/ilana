import cv2
import numpy as np
from matplotlib import pyplot as plt

#Lendo a imagem
img = cv2.imread("lena.jpg")

#Aplicando filtro blur
blur = cv2.GaussianBlur(img, (15,15),0)


#sobelX = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
#sobelY = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5)
#sobel = cv2.addWeighted(sobelX, 1, sobelY, 1 ,0)

result = cv2.addWeighted(img, 1, blur, 1, 0)
cv2.subtract (img, img2, dst, mask, dtype)

cv2.imshow("lena", result)
