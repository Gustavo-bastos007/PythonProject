#Faça um programa que mostre na tela uma contagem regressiva,
#para o estouro de fogos de artifícios, de 10 até 0
#com pause de um segundo

from time import sleep
for contagem in range(10,0, -1):
    print(contagem)
    sleep(0.7)
print('Feliz ANO NOVO!!!')