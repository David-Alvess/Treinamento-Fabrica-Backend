tuplaPalavras = ('Anciao', 'Legal', 'Fluminense', 'Lara')

vogais = ['a', 'e', 'i', 'o', 'u']

for palavra in tuplaPalavras:
    vogaisNaPalavra = []
    for letra in palavra:
        if letra.lower() in vogais:
            vogaisNaPalavra.append(letra)
    print ('Vogais da palavra {}: {}' .format(palavra, vogaisNaPalavra))