import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("coins.png", 0)

#img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

title = 'binaria'

images = [img, thresh1]
plt.subplot(),plt.imshow(thresh1,'gray')
plt.title(title)

mediana = cv2.medianBlur(thresh1, 5)
cv2.imshow("mediana", mediana)

lower_yellow = np.array([255,255,0])
upper_yellow = np.array([255,255,0])

hsv = cv2.cvtColor(mediana, cv2.COLOR_BGR2HSV)

yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

cv2.imshow("yellow", yellow)

plt.show()




