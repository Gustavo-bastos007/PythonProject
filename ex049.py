#tela que mostre todos os números pares que
# estão no intervalo de  1 até 50


for numero in range(1,51):
    print('.', end="")
    if numero % 2 == 0:
      print(numero, end='')
print('Fim')

# ou
# for numero in range(2,51,2):
#    print(numero, end='')
#print('FIM')
#nesse caso diminui as interações para 25 interações oa inves de 50 do codigo anterior

