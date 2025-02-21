#desenvolver um programa que leia o nome, idade e sexo de 4 pessoas
#No final do programa, mostre
#a media de idade do grupo.
#qual é nome do homem mais velho


somaidade = 0
mediaidade = 0
maoiridadehomem = 0
nomevelho = ''
for people in range(1,5):
    print('-----{}º Pessoa------'.format(people))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if people ==1 and sexo in 'Mm':
        maoiridadehomem =idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maoiridadehomem:
        maoiridadehomem = idade
        nomevelho = nome
mediaidade = somaidade /4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maoiridadehomem,nomevelho))
