
listaNumeros = []

while True:
    numero = int(input('Informe um numero ou digite 0 para sair: '))

    if numero == 0:
        break
    else:
        listaNumeros.append(numero)

qtdeNumeroDigitados = len(listaNumeros)
listaDecrescente = sorted(listaNumeros, reverse=True)
cincoDigitado = listaNumeros.count(5)

print('Quanditdade de numeros digitados: {}' .format(qtdeNumeroDigitados))
print('Lista em ordem decrescente: {}' .format(listaDecrescente))
print('O numero 5 foi digitado {} vezes '.format(cincoDigitado))