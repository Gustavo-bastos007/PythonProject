# A confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta emostre sua categoria de acordo com a idade
# até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos junior
#até 25 anos senior
# acima de 25: master

from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação MIRIM.')
elif idade > 9 and idade <=14:
    print('Classificão INFANTIL.')
elif idade <=19:
    print('Classificação JUNIOR')
elif idade <=25:
    print('Claificação SENIOR')
else:
    print('Classificação Master')