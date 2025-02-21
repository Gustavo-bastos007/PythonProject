#Computador vai "pensar" em número entre 0 á 10. Só que agora o jogador
#vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessarios para vencer

from random import randint
computador = randint(0,10)
print('Sou seu computador.... Acabei de pensar em numero entre 0 e 10')
print('Será que vc consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais.. tente mais uma vez")
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Você acertou! com {} palpites'.format(palpite))