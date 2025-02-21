#escreva um programa que leia 2 numeros inteiros e compare-os
# mostrando na tela uma mensagem
# o primeiro valor é maior
# o segundo valor é maior
# os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os valores são iguais')
