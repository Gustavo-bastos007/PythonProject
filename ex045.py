#pedra papel e tesoura
from os import PRIO_PGRP
from random import randint
itens =('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
#print('O computador escolheu {}'.format(itens[computador]))
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 10) #linhas
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('Computador venceu')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Computador vence')
    elif  jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('compuatador vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')




