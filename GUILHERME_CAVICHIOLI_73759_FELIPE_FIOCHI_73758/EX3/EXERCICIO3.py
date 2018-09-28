import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')


borrado = cv2.GaussianBlur(img, (15,15),0)
subtrair = cv2.subtract(img,borrado)
mistura = cv2.addWeighted(img, 0.1, borrado, 1, 0)


plt.subplot(121), plt.imshow(img), plt.title('original')
plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(mistura), plt.title('borrada')
plt.xticks([]), plt.yticks([])
plt.show()
