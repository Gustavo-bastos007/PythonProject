#Cri eum algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
numero = float(input('Digite um número'))
dobro = numero * 2
triplo = numero * 3
rai = numero ** (1/2)
print(' O dobro de {} vale {}.' .format(numero, dobro))
print('O triplo de {} vale {}. \n Já a raiz quadrada de {} é igual á {}'.format(numero, triplo, numero, rai))