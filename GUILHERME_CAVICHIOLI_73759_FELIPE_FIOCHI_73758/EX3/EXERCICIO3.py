import cv2
import numpy as np
import matplotlib.pyplot as plt

#Plotando as imagens
predio1 = cv2.imread('predios1.png', 0)
predio2 = cv2.imread('predios2.png', 0)

#Equalizando os histogramas
predio1_H1 = cv2.equalizeHist(predio1)
predio1_H2 = cv2.equalizeHist(predio2)

#Estabilizada
plt.subplot(421),plt.imshow(predio1,'gray'),plt.title('Original Predio_1')
plt.subplot(423),plt.imshow(predio1_H1,'gray'),plt.title('Estabilizada Predio_1')

plt.subplot(425),plt.imshow(predio2,'gray'),plt.title('Original Predio_2')
plt.subplot(427),plt.imshow(predio1_H2,'gray'),plt.title('Estabilizada Predio_2')

#
plt.subplot(422),plt.hist(predio1.ravel(),256,[0,256]),plt.title('Histograma - Original Predio_1')
plt.subplot(424),plt.hist(predio1_H1.ravel(),256,[0,256]),plt.title('Histograma - Estabilizada Predio_1')

plt.subplot(426),plt.hist(predio2.ravel(),256,[0,256]),plt.title('Histograma - Original Predio_2')
plt.subplot(428),plt.hist(predio1_H2.ravel(),256,[0,256]),plt.title('Histograma - Estabilizada Predio_2')

plt.show()
