import cv2
# Biblioteca para plotar imagem com os eixos
from matplotlib import pyplot as plt

#Biblioteca para trabalhar com numeros
import numpy as np

imagem = cv2.imread("layne-staley2.jpg")
#cv2.imshow("Original", imagem)

#Determinando os metodos de cores que será convertido
#No caso, em tons de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#fig representa o plt
fig, ((primeira, segunda), (terceira, quarta)) = plt.subplots(2,2)

primeira.imshow(cinza, cmap='gray')

segunda.hist(cinza.flatten(), 256, range=(0,255))


#Equalizando a imagem
nova = cv2.equalizeHist(cinza)

terceira.imshow(nova, cmap='gray', interpolation='bicubic')

quarta.hist(cinza.flatten(), 256, range=(0,255))

plt.show()
