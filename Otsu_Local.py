import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('abobora.tif', 0) #faz a leitura da imagem

plt.imshow(img, cmap='gray') #plota a imagem
plt.title("Imagem 'abobora.tif'") #adiociona um titulo a imagem
plt.show() #mantem a imagem plotada

#metodo Otsu
thresh_Otsu = threshold_otsu(img) #aplica o threshold na imagem utilizando metodo Otsu
img_out = img > thresh_Otsu
img_out_inv = 255-img_out #calcula o negativo da imagem
plt.imshow(img_out_inv, cmap='gray') #plota a imagem
plt.title("Imagem com aplicação do método de Otsu na imagem total") #adiciona titulo a imagem
plt.show() #mantem a imagem plotada


#***************divisao em 8 sub-imagens**************
width = int(img.shape[0]/8) #recebe o tamanho da imagem

[img_vct_8, img_out_seg_8] = [[], []] #inicializa o vetor que recebera a imagem segmentada

for i in range(8):
    img_vct_8.append(img[:,width*i:width*(i+1)]) #separa a imagem
    thresh_Otsu = threshold_otsu(img_vct_8[i]) #aplica o threshold na imagem utilizando metodo Otsu
    img_out = img_vct_8[i] > thresh_Otsu
    img_out_inv = 255-img_out #calcula o negativo da imagem
    img_out_seg_8.append(img_out_inv) #armazena o resultado no vetor


[cont, matriz_out_8, matriz_8] = [0, [], []] #inicializa as variaveis
for i in range(4): 
    matriz_out_8.append(np.concatenate((img_out_seg_8[i+cont], img_out_seg_8[i+cont+1]), axis = 1)) #concatena as matrizes
    cont = cont+1 #incrementa variavel auxiliar

matriz_8 = np.concatenate((matriz_out_8[0], matriz_out_8[1], matriz_out_8[2], matriz_out_8[3]), axis = 1)#concatena as matrizes


plt.imshow(matriz_8, cmap='gray') #plota a imagem
plt.title("Imagem com divisão em 8 sub-imagens (método de Otsu)") #adiciona um titulo a imagem
plt.show() #mantem a imagem plotada


#***************divisao em 32 sub-imagens**************
width = int(img.shape[0]/32) #recebe o tamanho da imagem

[img_vct_32, img_out_seg_32] = [[], []] #inicializa o vetor que recebera a imagem segmentada

for i in range(32):
    img_vct_32.append(img[:,width*i:width*(i+1)]) #separa a imagem
    thresh_Otsu = threshold_otsu(img_vct_32[i]) #aplica o threshold na imagem utilizando metodo Otsu
    img_out = img_vct_32[i] > thresh_Otsu
    img_out_inv = 255-img_out #calcula o negativo da imagem
    img_out_seg_32.append(img_out_inv) #armazena o resultado no vetor


[cont, matriz_out1_32, matriz_out2_32, matriz_32] = [0, [], img_out_seg_32, []] #inicializa as variaveis
for j in range(5):
  cont=0
  for i in range(16//(2**j)):
    if((j%2) == 0): #intercala o vetor que vai receber as imagens concatenadas
      matriz_out1_32.append(np.concatenate((matriz_out2_32[i+cont], matriz_out2_32[i+cont+1]), axis = 1)) #concatena as matrizes
      cont = cont+1 #incrementa a variavel auxiliar
      if(i==(16//(2**j)-1)):matriz_out2_32 = [] 
    elif(j%2 != 0): #intercala o vetor que vai receber as imagens concatenadas
      matriz_out2_32.append(np.concatenate((matriz_out1_32[i+cont], matriz_out1_32[i+cont+1]), axis = 1)) #concatena as matrizes
      cont = cont+1 #incrementa a variavel auxiliar
      if(i==(16//(2**j)-1)): matriz_out1_32 = []

plt.imshow(matriz_out1_32[0], cmap='gray') #plota a imagem
plt.title("Imagem com divisão em 32 sub-imagens (método de Otsu)") #adiciona um titulo a imagem
plt.show() #mantem a imagem plotada  


#***************divisao em 256 sub-imagens**************
width = int(img.shape[0]/256) #recebe o tamanho da imagem

[img_vct_256, img_out_seg_256] = [[], []] #inicializa o vetor que recebera a imagem segmentada

for i in range(256):
    img_vct_256.append(img[:,width*i:width*(i+1)]) #separa a imagem
    thresh_Otsu = threshold_otsu(img_vct_256[i]) #aplica o threshold na imagem utilizando metodo Otsu
    img_out = img_vct_256[i] > thresh_Otsu
    img_out_inv = 255-img_out #calcula o negativo da imagem
    img_out_seg_256.append(img_out_inv) #armazena o resultado no vetor


[cont, matriz_out1_256, matriz_out2_256, matriz_256] = [0, [], img_out_seg_256, []]
for j in range(7):
  cont=0
  for i in range(128//(2**j)):
    if((j%2) == 0):  #intercala o vetor que vai receber as imagens concatenadas
      matriz_out1_256.append(np.concatenate((matriz_out2_256[i+cont], matriz_out2_256[i+cont+1]), axis = 1)) #concatena as matrizes
      cont = cont+1
      if(i==(128//(2**j)-1)):matriz_out2_256 = []
    elif(j%2 != 0): #intercala o vetor que vai receber as imagens concatenadas
      matriz_out2_256.append(np.concatenate((matriz_out1_256[i+cont], matriz_out1_256[i+cont+1]), axis = 1)) #concatena as matrizes
      cont = cont+1 #incrementa a variavel auxiliar
      if(i==(128//(2**j)-1)): matriz_out1_256 = []

matriz_256 = np.concatenate((matriz_out1_256[0], matriz_out1_256[1]), axis = 1)#concatena as matrizes

plt.imshow(matriz_256, cmap='gray') #plota a imagem
plt.title("Imagem com divisão em 256 sub-imagens (método de Otsu)") #adiciona um titulo a imagem
plt.show() #mantem a imagem plotada 
