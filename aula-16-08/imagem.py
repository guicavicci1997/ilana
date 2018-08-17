import cv2

#Le imagem
imagem = cv2.imread("timao.png")

#Exibe imagem
cv2.imshow("Timao", imagem)

#Shape tem tres informacoes, altura, largura e canais nas seguintes posicoes
#De vetores
print("Altura= ", imagem.shape[0])
print("Largura= ", imagem.shape[1])
print("Canais= ", imagem.shape[2])

#Opencv utiliza o padrão BGR

#Acessar um pixel da imagem
(b,g,r) = imagem[100,200]

#print ("azul = ", b, "verde = ", c, "vermelho = ", r)

#Nesse caso em especifico eu quero so o tom de vermelho do pixel,
#b[0], g[1], [r][2]
vermelho = imagem [110,210,2]

#Exemplo utilizando interpolacao de string em python
print(f"vermelho = {vermelho}")

#Pinta de vermelho o pixel
imagem[100,200] = (0,0,255)

#Pinta uma região da imagem de vermelho
imagem[110:125 ,210:260] = (0,0,255)


#Exibe imagem
cv2.imshow("Timao", imagem)

#Cria uma nova imagem
cv2.imwrite("timaonovo.png", imagem)
