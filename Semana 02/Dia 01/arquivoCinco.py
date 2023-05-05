
pesos = []

for i in range (1, 6):
    peso = float(input("Informe o peso: "))
    pesos.append(peso)

menorPeso = min(pesos)
maiorPeso = max(pesos)


print("O menor peso é {:.2f}KG" .format(menorPeso))
print("O maior peso é {:.2f}KG" .format(maiorPeso))