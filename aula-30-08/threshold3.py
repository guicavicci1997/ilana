import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('mt-03.png', 0)
kernel = np.ones((5,5),np.uint8)
th3 = cv2.threshold(img,127,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.cv2.THRESH_BINARY,11,2)
erosion = cv2.erode(img,kernel,iterations = 1)
fig, (o, e, t) = plt.subplots(1,3)
o.imshow(img, cmap="gray")
o.set(title="Imagem Original")
e.imshow(erosion)
e.set(title="Imagem com Erosão")
plt.show()
