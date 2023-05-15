from random import randint

lista_de_numeros = []

for i in range (0, 5):
    numeroAleatorio = randint(0, 100)
    lista_de_numeros.append(numeroAleatorio)

tupla_de_numeros = tuple(lista_de_numeros)

maiorNumero = max(tupla_de_numeros)
menorNumero = min(tupla_de_numeros)
print('''
        Os numeros da tupla são: {} 
        Menor valor na tupla: {}
        Maior valor na tupla: {}''' .format(tupla_de_numeros, menorNumero, maiorNumero))
