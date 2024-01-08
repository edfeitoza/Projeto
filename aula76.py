""" 
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

# Exemplo de dicionario de dados

# pessoa = {
#     "nome": "Python",
#     "Sobrenome": "Linguagem",
#     "Idade": 20,
#     "Altura": 1.85,
#     "Endereços": [
#         {"rua": "sem saida", "numero": 0},
#         {"rua": "entroncamento 1", "numero": 13},
#     ],
# }

# print(pessoa['nome'])
# print(pessoa['Idade'])

# print(20*'-')

# for chave in pessoa:
#     print(chave, pessoa[chave])

####################################

#Dicionarios com chaves dinâmicas

pessoa = {}


pessoa['nome'] = 'Python'
print(pessoa)
print(pessoa['nome'])

print(20*'-')

chave = 'nome_completo'

pessoa[chave] = 'Python'
pessoa['apelido'] = 'Programacao'

print(pessoa[chave])
print(pessoa['apelido'])

del pessoa['apelido']
print(pessoa)

if pessoa.get('apelido') is None:
    print('Nao existe!!!')
else:
    print(pessoa['apelido'])
