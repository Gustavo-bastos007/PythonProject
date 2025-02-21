# crie um programa que leia duas notas de um aluno e calcule a media
# mostrando uma mensagem no final de acordo com a nota media
#media abaixo de 5: reprovado
#media entre 5. e 6,9: recuperação
#media 7 ou supeiror: aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media =(n1 + n2)/2
print('Com as notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 5 and media <7:
    print('Aluno em RECUPERAÇÃO')
elif media >= 7:
   print('Aluno APROVADO!')
elif media < 5:
    print("Aluno REPROVADO")
