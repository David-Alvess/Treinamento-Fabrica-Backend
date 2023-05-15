todosOsNumeros = []
numerosImpares = []
numerosPares = []

quantidade_de_Numeros = int(input('Quantos numeros você quer inserir? '))

for i in range(quantidade_de_Numeros):
    numeroInformado = int(input('Informe o {}º numero: ' .format(i+1)))
    todosOsNumeros.append(numeroInformado)

    if numeroInformado % 2 == 0:
        numerosPares.append(numeroInformado)
    else:
        numerosImpares.append(numeroInformado)

print('''
Todos os numeros: {}
Numeros pares: {}
Numeros impares: {}
''' .format(todosOsNumeros, numerosPares, numerosImpares))