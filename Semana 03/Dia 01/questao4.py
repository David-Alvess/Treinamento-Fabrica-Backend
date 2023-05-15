lista_de_numeros = []

for i in range (5):
    numero = int(input('Informe o {}º numero para inserir na lista: ' .format(i+1)))
    lista_de_numeros.append(numero)

maiorNumero = max(lista_de_numeros)
menorNumero = min(lista_de_numeros)
posicao_maior_numero = lista_de_numeros.index(maiorNumero)
posicao_menor_numero = lista_de_numeros.index(menorNumero)

print('''
{} é o menor valor da lista e sua posição é {}
{} é o maior valor da lista e sua posição é {}
''' .format(menorNumero, posicao_menor_numero, maiorNumero, posicao_maior_numero))