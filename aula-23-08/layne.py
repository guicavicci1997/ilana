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
fig, (primeira, segunda, terceira) = plt.subplots(1,3)

primeira.imshow(imagem)

#Setando labels da primeira imagem
primeira.set(xlabel = 'largura', ylabel = 'altura', title='Layne colorido')



#Cmap determina que sera em tons de cinza
segunda.imshow(cinza, cmap='gray')
terceira.imshow(imagem)

#Salvando a imagem modificada
fig.savefig("teste.png")

#plt.subplot(121),plt.imshow(imagem)
#plt.subplot(122),plt.imshow(imagem)

plt.show()

