# Faça um programa que leia a largura e altura de uma parede em metros.
#calcule  a sua área e a quantidade de tinta necessária para pinta´-la,
#sabendo que cada litro de tinta, pinta uma area de 2m quadrados

larg = float(input('Digite a lagura da parede'))
alt = float(input('Digite a altura da parede'))
área = larg * alt
print('Sua parede tem a dimenção de {} x {} e sua área é de {}m².'.format(
    larg, alt, área
))
tinta = área / 2
print('Para pintar essa parede, você precisa de {}L de tinta'.format(tinta))