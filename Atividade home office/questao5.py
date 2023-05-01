salario = float(input("Informe o salário recebido: "))
gasto_em_despesas = float(input("Informe o valor gasto em despesas: "))

if salario >= gasto_em_despesas:
    print("Gastos dentro do orçamento!")
else:
    print("Gastos fora do orçamento!")