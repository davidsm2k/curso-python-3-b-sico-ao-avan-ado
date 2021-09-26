carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total_preco = sum([produto[1] for produto in carrinho])

print(total_preco)

