#Faça um programa que leia um peso de 5 pessoas. no final, mostre
#qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {}ºpessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('E o menor peso foi de {}Kg'.format(menor))
