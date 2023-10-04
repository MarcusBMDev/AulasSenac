nomes_produtos = ["Produto A", "Produto B", "Produto C"]
valores_produto = [100.0, 200.0, 150.0]
quantidade = [100, 100, 100]
valores_frete = [50.00, 40.00, 10.00]


imposto1 = (0.12) #12%
imposto2 = (0.06) #6%
imposto3 = (0.03) #3%
valores_custos = [] #Coloquei esse array para armazenar os resultados de cada produto. Que é usado no segundo for. Pois sem ele estaria apenas puxando o ultimo produto, que é o C.

for a in range(len(nomes_produtos)):
    valor_do_produto = valores_produto[a]
    frete = valores_frete[a]
    frete_por_produto = frete / quantidade[a]
    valor_custo = valor_do_produto + (valor_do_produto * (imposto1 + imposto2 + imposto3)) + frete_por_produto
    valor_venda = valor_custo * 1.60
    valores_custos.append((nomes_produtos[a], valor_custo, valor_venda))
for produto, custo, venda in valores_custos: 
    print(f"Produto: {produto}")
    print(f"Preço de custo: R${custo:}")
    print(f"Preço de venda: R${venda:}")
