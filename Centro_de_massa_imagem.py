def momentos(img_in):
    m = cv.moments(img_in)
    [m00, m10, m01, m11] = [m['m00'], m['m10'], m['m01'], m['m11']]

    return m00,m01,m10,m11 #retorna os valores

img_triang = cv.imread('triangulo.png', 0) #faz a leitura da imagem

m00, m01, m10, m11 = momentos(img_triang) #envia a imagem para a funcao do calculo do momento

xc_triang = m10/m00 #calcula o centro de massa coordenada x
yc_triang = m01/m00 #calcula o centro de massa coordenada y

print("A imagem 'triangulo.png' tem centro de massa nas cordenadas ({},{})".format(int(xc_triang), int(yc_triang)))


img_star = cv.imread('estrela.png', 0) #faz a leitura da imagem

m00, m01, m10, m11 = momentos(img_star) #envia a imagem para a funcao do calculo do momento

xc_star = m10/m00 #calcula o centro de massa coordenada x
yc_star = m01/m00 #calcula o centro de massa coordenada y

print("A imagem 'estrela.png' tem centro de massa nas cordenadas ({},{})".format(int(xc_star), int(yc_star)))

img_guit = cv.imread('guitarra.tif',0) #faz a leitura da imagem
img_banjo = cv.imread('banjo.tif',0) #faz a leitura da imagem

ret0, img_guit_resiz = cv.threshold(img_guit, 254, 255, cv.THRESH_BINARY_INV) #faz a binarização da imagem com limiar de 254
ret1, img_banjo_resiz = cv.threshold(img_banjo, 254, 255, cv.THRESH_BINARY_INV) #faz a binarização da imagem com limiar de 254

size_guit = len(img_guit) #tamanho da matriz
size_banjo = len(img_banjo) #tamanho da matriz

matriz_transf = cv.getRotationMatrix2D((size_guit/2, size_guit/2), 30, 0.25) #Matriz de transformação que reduz a imagem em 1/4, translada para o centro e rotaciona em 30 graus
guitarra_transf = cv.warpAffine(img_guit_resiz, matriz_transf, (size_guit, size_guit)) #Aplica a matriz de transformação para gerar a imagem final

matriz_transf = cv.getRotationMatrix2D((size_banjo/2, size_banjo/2), 30, 0.25) #Matriz de transformação que reduz a imagem em 1/4, translada para o centro e rotaciona em 30 graus
banjo_transf = cv.warpAffine(img_banjo_resiz, matriz_transf, (size_banjo, size_banjo)) #Aplica a matriz de transformação para gerar a imagem final

plt.imshow(guitarra_transf, cmap='gray') #plota a imagem
plt.title("Imagem 'guitarra.tif' redimensionada e rotacionada em 30º")
plt.show() #mantem a imagem plotada

plt.imshow(banjo_transf, cmap='gray') #plota a imagem
plt.title("Imagem 'banjo.tif' redimensionada e rotacionada em 30º")
plt.show() #mantem a imagem plotada

#Calculo dos momentos das imagens transformadas
moments_guit = cv.moments(img_guit)
HuMoments_guit = cv.HuMoments(moments_guit)

moments_banjo = cv.moments(img_banjo)
HuMoments_banjo = cv.HuMoments(moments_banjo)

#Calculo dos momentos das imagens transformadas
moments_guit_t = cv.moments(guitarra_transf)
HuMoments_guit_t = cv.HuMoments(moments_guit_t)

moments_banjo_t = cv.moments(banjo_transf)
HuMoments_banjo_t = cv.HuMoments(moments_banjo)

print("Momento de HU da guitarra após a transformação: \n{}\n\nMomento de Hu da guitarra antes da transformação: \n{}\n\n\n".format(HuMoments_guit_t, HuMoments_guit))
print("Momento de HU do banjo após a transformação: \n{}\n\nMomento de Hu do banjo antes da transformação: \n{}".format(HuMoments_banjo_t, HuMoments_banjo))

#calculo das distancias dos vetores HU
[dist_g, dist_b, dist_gt, dist_bt] = [0, 0, 0, 0]
for i in range(7): dist_b = dist_b + (HuMoments_banjo[i]**2)
dist_b = dist_b**(1/2)
for i in range(7): dist_g = dist_g + (HuMoments_guit[i]**2)
dist_g = dist_g**(1/2)
for i in range(7): dist_bt = dist_bt + (HuMoments_banjo_t[i]**2)
dist_b = dist_bt**(1/2)
for i in range(7): dist_gt = dist_gt + (HuMoments_guit_t[i]**2)
dist_g = dist_gt**(1/2)

print("\nDistância euclidiana do vetor HU do banjo sem transformação: {}\nDistância euclidiana do vetor HU do banjo após transformação: {}".format(dist_b, dist_bt))
print("\nDistância euclidiana do vetor HU da guitarra sem transformação: {}\nDistância euclidiana do vetor HU da guitarra após transformação: {}".format(dist_g, dist_gt))
