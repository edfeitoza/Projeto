
# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#filtragem comum
novos_produtos = [
    p for p in produtos
    if p['preco'] > 100
]

#Filtragem por MAP
novos_produtos_map = filter(
    lambda p: p['preco'] > 100,
    produtos
)

#Filtragem por funcao
def filtrar_preco(produto):
    return produto['preco'] > 100

#Filtragem por MAP chamando a funcao
novos_produtos_map = filter(
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos_map)
