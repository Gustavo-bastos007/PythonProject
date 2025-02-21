# programa que leia seis números inteiros e mostre a soma
#apenas que forem pares. se o valor digitado for impar desconsiderar

soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você informou {} números e a soma foi {}'.format(cont,soma))

