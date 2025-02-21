#INDICE DE MASSA CORPORAL
# Progrma que leia peso e altura de uma pessoa,
#calcule seu IMC e mostre seu status de acordo com a tabela abixo
#-Abaixo de 18.5: abaixo do peso
#- entre 18.5 and 25: peso ideal
# 25 até 30: sobrepeso
#30 até 40: obsidade
#Acima de 40: Obsidade Mórbida


peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso/(altura **2)## ** ao quadrado²
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBSIDADE')
else:
    print('Obsidade Mórbida')


