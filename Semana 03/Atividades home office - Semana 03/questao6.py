pessoas = []
maisPesados = []
maisLeves = []

while True:
    nome = input('Informe o nome ou digite "s" para sair: ')
    if nome.lower() == 's':
        break

    peso = float(input('Informe o peso: '))

    pessoa = {'nome': nome, 'peso': peso}
    pessoas.append(pessoa)

pessoaMaiorPeso = max(pessoas, key=lambda pessoa: pessoa['peso'])
maiorPeso = pessoaMaiorPeso['peso']
for pessoa in pessoas:
    if pessoa['peso'] == maiorPeso:
        maisPesados.append(pessoa)

pessoaMenorPeso = min(pessoas, key=lambda pessoa: pessoa['peso'])
menorPeso = pessoaMenorPeso['peso']
for pessoa in pessoas:
    if pessoa['peso'] == menorPeso:
        maisLeves.append(pessoa)

qtdePessoasCadastradas = len(pessoas)

print('Quantidade de pessoas cadastradas: {}'.format(qtdePessoasCadastradas))

print('A lista completa:')
for pessoa in pessoas:
    print('Nome:', pessoa['nome'], '- Peso:', pessoa['peso'])

print("Pessoa mais leve - Nome:", pessoaMenorPeso["nome"], "- Peso:", pessoaMenorPeso["peso"])
print("Pessoa mais pesada - Nome:", pessoaMaiorPeso["nome"], "- Peso:", pessoaMaiorPeso["peso"])
