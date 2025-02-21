#crie um programa que leia 2 valores e mostre um menu como:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do prgrama
# e realizar a solicitação em cada caso

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números/trocar numeros
    [5] sair do programa''')
    opacao = int(input('Qual é a sua opção? '))
    if opacao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual á {}'.format(n1, n2, soma))
    elif opacao == 2:
        mult = n1 * n2
        print('O resultado de {} X {} é igual a {}'.format(n1, n2, mult))
    elif opacao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior numero é {}'. format(n1, n2, maior))
    elif opacao == 4:
        print('Infome os números novamente:  ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opacao == 5:
        print('Finalizando...')
    else:
        print('Opçaõ inválida. Tente de novo')
    print("=-=" * 10)
print('Fim do  programa! Volte sempre')




