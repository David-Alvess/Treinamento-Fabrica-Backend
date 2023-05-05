
somaIdade = 0;
nomeHomemMaisVelho = "";
mulheresComMenosDeVinteAnos = 0;
idadeHomemMaisVelho = 0;

for i in range(4):
    nome = str(input("Informe o {}º nome: " .format(i + 1)))
    idade = int(input("Informe a idade da {}º pessoa: " .format(i + 1)))
    sexo = str(input("Informe o sexo da {}º pessoa (M/F): " .format(i + 1)))

    somaIdade += idade;

    if sexo.upper() == 'M' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade;
        nomeHomemMaisVelho = nome
        
    else:
        if idade < 20:
            mulheresComMenosDeVinteAnos += 1

mediaIdade = somaIdade / 4;

print('''
A media de idade do grupo é {}
O nome do homem mais velho é {}
O numero de mulheres com menos de 20 anos é {} 
''' .format(mediaIdade, nomeHomemMaisVelho, mulheresComMenosDeVinteAnos))