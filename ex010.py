#conversor de moedas
#U$1.00 = R$6.00
real = float(input('Informe quanto dinhiero vc tem?'))
dolar = real / 6.00
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))