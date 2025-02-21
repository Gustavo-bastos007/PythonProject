# crie um programa que leia o nome completo de uma pessoa e mmostre:
# o nome com todas a s letras maiusculas e minúsculas.
# Quantas letras ao total sem espaços
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome')
print('Seu nome em maiúsculas é {}'. format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
