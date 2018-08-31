import cv2
import numpy as np
from matplotlib import pyplot as plt


#Padrao colorido, 0 cinza, 1 depende do tom da imagem
img = cv2.imread("mt-03.jpg", 0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.ADAPTIVE_THRESH_MEAN_C)
ret,thresh3 = cv2.threshold(img,127,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()



