
pares = []
impares = []
todosOsNumeros = []

for i in range(5):
    numerosUsuario = float(input('informe o {}º numero:' .format(i +1)))
    todosOsNumeros.append(numerosUsuario)

    if numerosUsuario % 2 == 0:
        pares.append(numerosUsuario)
    else:
        impares.append(numerosUsuario)

pares.sort()
impares.sort()

print('Valores pares em ordem crescente: {}' .format(pares))
print('Valores impares em ordem crescente: {}' .format(impares))