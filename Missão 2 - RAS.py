#bibliotecas
import cv2
import numpy

#1a parte da missao
imagem = cv2.imread('passaro.jpg')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])


cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)
cv2.imwrite("saida.jpg", imagem)


#2a parte da missao

print('De qual pixel você quer os valores RGB?')
a=int(input('Cite o número da linha do pixel:'))
b=int(input('Cite o número da coluna do pixel:'))

imagem = cv2.imread('passaro.jpg')
(b,g,r) = imagem[a,b]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

#fim do codigo#bibliotecas
import cv2
import numpy

#1a parte da missao
imagem = cv2.imread('passaro.jpg')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])


cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)
cv2.imwrite("saida.jpg", imagem)


#2a parte da missao

print('De qual pixel você quer os valores RGB?')
a=int(input('Cite o número da linha do pixel:'))
b=int(input('Cite o número da coluna do pixel:'))

imagem = cv2.imread('passaro.jpg')
(b,g,r) = imagem[a,b]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

#fim do codigo