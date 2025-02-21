#Escreva um  programa que leia um numero inteiro qualquer e peça para o
# usúario escolher qual será a base de conversão
# 1 para binario
# 2 para octal
# 3 para Hexadecimal
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
opcao = int(input('Sua opção'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção inválida, tente novamente.')

