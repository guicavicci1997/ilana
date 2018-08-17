import cv2
import numpy as np


#Le imagem
imagem = cv2.imread("bola.png")

cv2.imshow("bola-amarela", imagem)

imagem[np.where((imagem == [0,255,255]).all(axis = 2))] = [255,255,255]


cv2.imshow("bola-branca", imagem)



