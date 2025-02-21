#Faça um lagoritmo que lei o sálario de um funcionario emostre seu novo sálario,
# com 15% de aumento.
salário = float(input( 'Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print( 'Um funcionánio que ganhava R${:.2f} com 15% de de aumento, passa a receber R${:.2f}'.format(salário, novo))