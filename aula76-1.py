# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

from traceback import print_tb


pessoa = {
    'nome': 'Python',
    'apelido': 'Programacao',
}

# # len - quantas chaves
# print(len(pessoa))

# # keys - iterável com as chaves
# print(pessoa.keys())

# # values - iterável com os valores
# print(pessoa.values())
# for valor in pessoa.values():
#     print(valor)

# # items - iterável com chaves e valores
# print(pessoa.items())
# print(list(pessoa.items()))
# for valor1 in pessoa.items():
#     print(valor1)

# for chave, valor in pessoa.items():
#     print(chave,valor)

# # setdefault - adiciona valor se a chave não existe
# pessoa.setdefault('idade',None) # type: ignore
# print(pessoa['idade'])

# copy - retorna uma cópia rasa (shallow copy)
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2,3],
}

#Não copia lista dentro de dicionarios
# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(f'Dicionario copiado na variavel D2  =>  {d2}')
# print(20*'*')
# print(f'Dicionario Original da Variavel D1 =>  {d1}')
# print(20*'*')

# deepcopy - faz uma cópia mais profunda, copiando inclusive dados mutaveis (listas)
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2,3],
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(f'Dicionario copiado na variavel D2  =>  {d2}')
# print(20*'*')
# print(f'Dicionario Original da Variavel D1 =>  {d1}')

p1 = {
    'nome': 'Python',
    'sobrenome': 'Programacao',
}

# popitem - Apaga o último item adicionado

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# update - Atualiza um dicionário com outro

# p1.update({
#     'nome': 'Novo_Nome',
#     'idade': 24,
    
# })
#########################################
#p1.update(nome='Valor_Novo', idade=35)

#########################################

tupla = (('nome', 'Novo Valor'),('idade', 30))
lista = [['nome', 'Valor Novo'], ['idade', 40]]

p1.update(tupla)
p1.update(lista)

print(p1)