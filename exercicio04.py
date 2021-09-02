premio = float(input("Digite o valor do prêmio: "))

imposto = (premio*0.93)

print("O valor do prêmio é de {} reais com o imposto de {} reais.\n O primeiro recebeu {} reais.\n O segundo {} reais.\n E o terceiro {} reais".format(imposto, (premio - imposto), (imposto*0.46), (imposto*0.32), (imposto*0.22)))