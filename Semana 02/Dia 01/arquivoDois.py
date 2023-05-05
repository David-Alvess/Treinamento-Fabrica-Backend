valorProduro = float(input("Informe o valor do produto: "))
formaDePagamento = int(input(
'''Insira a forma de pagamento: 
1 - A vista ou pix
2 - A vista no cartão
3 - Até 2x no cartão
4 - 3x ou mais no cartão 
'''))

if formaDePagamento == 1:
    valorProduro -= valorProduro * 0.10
    print("Valor total da compra: {:.2f}" .format(valorProduro))

elif formaDePagamento == 2:
    valorProduro -= valorProduro * 0.05
    print("Valor total da compra: {:.2f}" .format(valorProduro))

elif formaDePagamento == 3:
    print("Valor total da compra: {:.2f}" .format(valorProduro))

elif formaDePagamento == 4:
    valorProduro += valorProduro * 0.20
    print("Valor total da compra: {:.2f}" .format(valorProduro))

else:
    print("Digite uma opção de 1 a 4!")
