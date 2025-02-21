#Faça um programa que leia o sexo de uma pessoa, mas
# só aceite os valores M E f. CASO esteja errado, peça que digite
#novamnete o valor

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
idade = int(input('Informe sua idade: '))
print('fim do teste')