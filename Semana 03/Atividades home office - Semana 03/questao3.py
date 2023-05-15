
numeros = []

quantidade_de_numeros = int(input('Quantos numeros voce quer digitar? '))

i=0
while(i < quantidade_de_numeros):
    numeroInformado = int(input('informe o {}º numero: ' .format(i + 1)))

    if numeroInformado not in numeros:
        numeros.append(numeroInformado)
    i += 1

numeros.sort()
print('O numeros em ordem crescente: {}' .format(numeros))