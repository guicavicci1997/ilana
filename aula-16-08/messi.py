import cv2

#Le imagem
imagem = cv2.imread("messi.jpg")

bola = imagem[280:340, 330:390]

#Pegando a regiao abaixo e atribuindo os pixels recortados acima
#que representa a bola
imagem[273:333, 100:160] = bola

cv2.imshow ("bola", bola)

#Exibe imagem
cv2.imshow("messi", imagem)
