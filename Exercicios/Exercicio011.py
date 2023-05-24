altura = float(input("Digite a altura da parede: "))
largura  = float(input("Digite a largura da parede: "))

area = altura * largura
tinta = 2 * 2
qtd = area / tinta

print("A area da altura e largura da parede é {}".format(area))
print("E a quantidade de tinta usada para pintar essa parede eh: {}".format(qtd))