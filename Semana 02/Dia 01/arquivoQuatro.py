from datetime import date
anoAtual = date.today().year
maiorIdade = 0;
menorIdade = 0;

for i in range(1, 8):
    anoNascimento = int(input("Informe o ano de nascimento da {}º pessoa: " .format(i)))
    if anoAtual - anoNascimento <= 18:
        menorIdade += 1
    else: 
        maiorIdade += 1

print(
'''Numero de pessoas com mais de 18 anos: {}
Numero de pessoas com menos de 18 anos: {}''' .format(maiorIdade, menorIdade))