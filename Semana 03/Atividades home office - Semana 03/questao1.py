
listaValores = []

for i in range(4):
    numeroInformado = int(input('Informe o {}º numero: ' .format(i +1)))
    listaValores.append(numeroInformado)

tuplaValores = tuple(listaValores)

quantidade_de_noves = tuplaValores.count(9)
posicao_numero_tres = tuplaValores.index(3) if 3 in tuplaValores else 'nula'
pares = [valor for valor in tuplaValores if valor % 2 == 0]

print('O valor 9 aparece {} veze(s)' .format(quantidade_de_noves))
print('O primeiro valor 3 foi digitado na posição: {}' .format(posicao_numero_tres))
print('O valores pares é(são): {} ' .format(pares))
    