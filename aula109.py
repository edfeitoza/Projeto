# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator),sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['P','M','G','GG'],
    ['Masculino','Feminino','Unisex'],
    ['algodão','poliéster']
]
# print('Combinations')
# print_iter(combinations(pessoas, 2))

# print(20*'-')

# print('Permutations')
# print_iter(permutations(pessoas, 2))

print(20*'-')
print('Product')
print_iter(product(*camisetas))
