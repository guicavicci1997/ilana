#pip3 install opencv-python

import cv2
#import numpy as np
#from matplotlib import pyplot as plt

cap=cv2.VideoCapture("cloth2.avi")

while(True):

    
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #tupla é um objeto
    #threshowd de binarizacao para binarizar a imagem, ou seja deixar em preto e branco
    #ou preto ou branco
    ret2, binaria = cv2.threshold(gray,100, 255,cv2.THRESH_BINARY)

    #cv2.imshow("binaria", binaria)

    #aplicando filtro para remover ruidos
    mediana = cv2.medianBlur(frame, 5)
    #cv2.imshow("mediana", mediana)


    #Aplicando filtro canny

    edges = cv2.Canny(gray, 100,200)
    cv2.imshow("canny", edges)


    cv2.imshow("gray", gray)

    #sobel determina horizontal, vertical e

    sobelX = cv2.Sobel(gray, cv2.CV_64F,1,0,ksize=5)
    sobelY = cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=5)

    #pega uma porcentagem da primeira imagem
    #uma porcentagem da segunda imagem e um terceiro elemento
    #para gerar uma terceira imagem
    sobel = cv2.addWeighted(sobelX, 1, sobelY, 1 ,0)

    cv2.imshow("sobel", sobel)
    
    #Condicao de parada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Libera a captura
cap.release()
#Destroi as telas
cv2.destroyAllWindows()






