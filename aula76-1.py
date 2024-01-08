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

pessoa = {
    'nome': 'Python',
    'apelido': 'Programacao',
}

# len - quantas chaves
print(len(pessoa))

# keys - iterável com as chaves
print(pessoa.keys())

# values - iterável com os valores
print(pessoa.values())
for valor in pessoa.values():
    print(valor)

# items - iterável com chaves e valores
print(pessoa.items())
print(list(pessoa.items()))
for valor1 in pessoa.items():
    print(valor1)

for chave, valor in pessoa.items():
    print(chave,valor)

# setdefault - adiciona valor se a chave não existe
pessoa.setdefault('idade',None) # type: ignore
print(pessoa['idade'])
