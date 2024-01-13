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

#Mapeamento de dados em list comprehension

# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 20, },
#     {'nome': 'p3', 'preco': 200, },
#     {'nome': 'p4', 'preco': 800, },
#     {'nome': 'p5', 'preco': 100, },
#     {'nome': 'p6', 'preco': 760, },
# ]

# novos_produtos = [
#     produto
#     for produto in produtos
# ]

# # print(*novos_produtos, sep='\n')

#################################################

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     for produto in produtos
    
# ]
# print(*novos_produtos, sep='\n')

#################################################

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}         #Mapeamento corresponde em pegar informações e
#     for produto in produtos                           #transformar em outra lista do mesmo tamanho
    
# ]
# print(*novos_produtos, sep='\n')

#################################################

#Aplicando Filtro

#################################################

#List comprehension

# lista = [
#     n for n in range(10)
#     if n < 5    
# ]
# print(lista)

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 20, },
    {'nome': 'p3', 'preco': 200, },
    {'nome': 'p4', 'preco': 800, },
    {'nome': 'p5', 'preco': 100, },
    {'nome': 'p6', 'preco': 760, },
]

n_produtos = [
    {**produto, 'preco': produto['preco']}
    for produto in produtos
    if (produto['preco']) > 20              #Filtragem da lista
]

p(n_produtos)

