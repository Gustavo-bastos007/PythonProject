#calculando preço
#Faça um programa que leia o preço de um produto e mostre seu novo preço
# com 5%de desconto.

preco = float(input('Digite o preço do produto? R$:'))
novo = preco - (preco*5 / 100)
print('O produto que custava  R${}'. format(preco))
print('na  promoção com desconto de 5% vai custar R${}'.format(novo))
