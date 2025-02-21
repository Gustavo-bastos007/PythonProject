#Analiador de triângulos
# tipo de tringulo será formado
#EQUILÁTERO: TODOS OS LADOS IGUAIS
#ISÓSCELES: DOIS LADOS IGUAIS
#ESCALENO: TODOS LADOS DIFERENTES
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem forma um triângulo! ', end ='')
    if r1 == r2 and r2 == r3: # r1 == r2 ==r3 (mesma coisa)
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo')