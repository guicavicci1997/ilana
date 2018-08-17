import cv2
import numpy as np


#Le imagem
imagem = cv2.imread("messi.jpg")

#wawpaffine - aplica as transformadas a partir de uma matriz criada

cv2.imshow("imagem", imagem)

#Escala

#Pegando da minha imagem os dois primeiros parametros :2
altura, largura = imagem.shape[:2]

#dobrando tamanho da altura e da largura
nova = cv2.resize(imagem, (2*largura, 2*altura),
                  interpolation = cv2.INTER_CUBIC)


##interpolation 3 tipos linear=padrao
#cubic=para aumentar sem distorcao
#area=para diminuir
cv2.imshow("imagem nova", nova)

#Mover 80 posicoes em x e 30 posicoes em y

#Criacao da matriz de translacao
##Matriz = np.float32([[1,0,80], [0,1,30]])

#Criacao da matriz de rotação
Matriz = cv2.getRotationMatrix2D((largura/2, altura/2), 90, 1)

print (Matriz)

nova = cv2.warpAffine(imagem, Matriz, (largura,altura))

cv2.imshow("imagem nova", nova)

