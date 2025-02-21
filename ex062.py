#Progrma que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão
# primeiro  = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 - 1) * razao
# for c in range(primeiro, decimo + razao, razao):
#   print('{}'.format(c), end=".")

#agora com while
print("-=" * 10)
print('Gerador de PA')
print("-=" * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print("Fim")

