altura = float(input("Digite a altura desejada da parede em metros: "))
comprimento = float(input("Digite o comprimento desejado da parede em metros: "))

area = (altura*comprimento)
cobrimento = (area/3)
latas = (cobrimento//3.6)
total = (latas*107.00)


print("Você terá que comprar um total de {:.0f} latas de tinta que custarão {:.2f} reais.".format(latas, total))

