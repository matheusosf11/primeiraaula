produto = input("Digite o nome do produto: ")
custo = float(input("Digite o valor do custo do produto: "))
preco_de_venda = float(input("Digite o valor do preco do venda: "))
lucro = preco_de_venda - custo
bom = lucro>20

print("O produto",produto,"tem um custo de R$",custo,"e o preço de venda de R$",preco_de_venda,"ficando com um lucro de R$",lucro)
print("O lucro foi bom?",bom)