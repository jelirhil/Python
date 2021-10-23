estoque = {"tomate": [1000, 2.30],
"alface": [500, 0.45],"batata":[2001, 1.20],"feijao":[100,1.50]}
venda = [ ["tomate", 5],["batata", 10],["alface", 5] ]
total=0
print("Vendas:\n")
for operacao in venda:
    produto,quantidade= operacao
    preco = estoque[produto]
    custo = preco * quantidade
    print("{0}: {1} x {2} = {3}" .format (produto,quantidade,preco,custo))
    estoque[produto][0] -= quantidade
    total+=custo
print("Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print("Preco: %6.2f\n" %dados[1]) 