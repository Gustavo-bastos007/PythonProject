#elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#- á vista dinheiro ou pix: 10% de desconto
# á vista no cartão 5% de desconto
# e, até 2x no cartão preço normal
#3x ou mais no cartão 20% de juros.

print('{:=^40}'.format(' Lojas gustavos '))
preco = float(input('Preço das compras: R$ '))
print('''Formas de pagamentos
[1] á vista dinheiro ou Pix
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual á opção: '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total /2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparcelas = int(input('Quantas parcelas?'))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparcelas, parcela))
else:
    total = preco
    print('Opção invalida, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
