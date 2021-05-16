carrinho = []
produtos = list(range(5))
preços = list(range(10, 51, 10))

compras = list(zip(produtos, preços))

total = sum([preço for  produto,preço in compras])
print(total)
