#Excreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa o programa vai perguntar o valor da casa, o sálario
# do comprador e em quantos anos ele vai pagar

# calcule o valor da prestação mensal sabendo que ela não pode exceder 30%
# do salario ou então o emprestimo será negado

casa = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa /(anos * 12)
minimo = salario * 30 /100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestacao))
if  prestacao <= minimo:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')



