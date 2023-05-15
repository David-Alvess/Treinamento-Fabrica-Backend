
todosOsNumeros = []
numerosPares = []
numerosImpares = []

while True:
    numeroDigitado = int(input('Digite o numero ou 0 para sair: '))
    
    if numeroDigitado != 0:
        todosOsNumeros.append(numeroDigitado)
        if numeroDigitado % 2 == 0:
            numerosPares.append(numeroDigitado)
        else: numerosImpares.append(numeroDigitado)
    else:
        break

print('Todos os numeros digitados: {}' .format(todosOsNumeros))
print('Numeros pares: {}' .format(numerosPares))
print('Numeros impares: {}' .format(numerosImpares))
