#crie um progrma que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
# já são maiorres.

from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0
for pessoas in range(1,8):
    nasc = int(input('Em que ano {}º a pessoa nasceu? '.format(pessoas)))
    idades = atual - nasc
    print("Essa pessoa tem {} anos".format(idades))
    if idades >= 18:
        print('Essa pessoa é maior de idade')
        totmaior +=1
    else:
        print('Essa essoa é menor de idade')
        totmenor +=1
print('Tivemos ao todo {} pessoas maiores de idade'.format(totmaior))
print('E {} pessoas menores de idade'.format(totmenor))
