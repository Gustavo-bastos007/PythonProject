#Faça um progrma que leia o ano de nascimento de uma pessoa e infome,
# de acordo com sua idade, se ela ainda vai se alistar ao serviço militar obrigatorio
# se é tempo de se alistar ou se já paasou do tempo do alistamento.
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo.#

from datetime import date
atual = date.today().year
nasci = int(input('Informe o ano do seu nascimento'))
idade = atual - nasci
print('Quem nasceu em {} tem {} anos em {}'. format(nasci, idade, atual))
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = idade - 18
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento'.format(saldo))

    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
    
elif idade > 18:
    saldo = idade - 18
    print('Você já deviria ter se alistado há {} anos,'.format(saldo))
    
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
