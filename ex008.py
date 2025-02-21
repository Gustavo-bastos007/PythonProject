#conversor de medidas
#escreva um program que leia um valor em metros e exiba convertido em centímetro

medida = float(input('Informe a distância em metros'))
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {:.1f}cm e {:.1f}mm'. format(medida,cm, mm))
