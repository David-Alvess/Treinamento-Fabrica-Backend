while True:

    valor_um = float(input("Informe o primeiro valor: "))
    valor_dois = float(input("Informe o segundo valor: "))

    opcao = int(input(
    '''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] VER MAIOR NUMERO
    [4] INSERIR NUMEROS NOVOS
    [5] SAIR

    Digite uma opção:
    '''))

    resultado = 0;

    if opcao == 1:
        resultado = valor_um + valor_dois;
        print("Soma = {:.2f}" .format(resultado))
    elif opcao == 2:
        resultado = valor_um * valor_dois;
        print("Multiplicação = {:.2f}" .format(resultado))
    elif opcao == 3:
        print("O maior numero é {} " .format(max(valor_um, valor_dois)))
    elif opcao == 4:
        continue
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção válida!")