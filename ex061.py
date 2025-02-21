#Faça um programa que leia um número qualquer e meostre o seu fatorial

##from math import factorial
# n = int(input('Digite um número para calcular o seu Fatorial'))
# f = factorial()
# print('O fatorial de {} é {}'.format(n,f))

n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
