import random

jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4',]
resultados = {}

for jogador in jogadores:

    numeroSorteado = random.randint(1, 6)
    resultados[jogador] = numeroSorteado

print('Resultado: ')
for jogador, numeroSorteado in resultados.items():
    print(jogador + ' tirou' , numeroSorteado)


vencedor = max(resultados, key=resultados.get)
print('O vencedor é o {}' .format(vencedor))