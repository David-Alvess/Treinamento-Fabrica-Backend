produtos = (
    ('Produto 1', 5.99),
    ('Produto 2', 10.00),
    ('Produto 3', 8.65),
    ('Produto 4', 17.50),
    ('Produto 5', 19.99),
)

print('PRODUTO \tPREÇO')

for produto, preco in produtos:
    print(f'{produto} \tR${preco:.2f}')