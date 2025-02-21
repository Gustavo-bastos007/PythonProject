#crie um programa que leia varios números inteiros pelo teclado.
#O progrma só vai para quando o usuário digitar o valor 999,
#que é a condição de parada. N o final mostre quntos numeros foram
#digitados e qual foi a soma entre eles(desconsiderando o flag).

#num = 0
#cont = 0
#soma = 0
# é igual a
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números.'.format(cont))
print('E soma entre eles foi {}'.format(soma))
print('Acabou')