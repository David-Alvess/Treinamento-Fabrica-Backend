import random

numeroDeJogos = int(input('Quantos jogos você quer gerar? '))
listaSorteada = []

for i in range(numeroDeJogos):
    listaCincoNumeros = []

    for i in range(5):
        numeroGerado = random.randint(1,50)
        listaCincoNumeros.append(numeroGerado)
    
    listaSorteada.append(listaCincoNumeros)

print('Jogos sorteados: {}' .format(listaSorteada))
