# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# Criando uma lista automaticamente

# print(list(range(10)))

# print(20*'|')

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# print(20*'|')

# lista = [numero for numero in range(20)]
# print(lista)

# print(20*'|')

# lista = [
#     numero * 3 
#     for numero in range(20)
# ]
# print(lista)

#MApeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 200, },
    {'nome': 'p3', 'preco': 50, },
    {'nome': 'p4', 'preco': 800, },
    {'nome': 'p5', 'preco': 100, },
    {'nome': 'p6', 'preco': 760, },
]

# novos_produtos = [
#     produto
#     for produto in produtos
# ]

# print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
    
]
print(*novos_produtos, sep='\n')