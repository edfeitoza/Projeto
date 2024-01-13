# Dictionary Comprehension e Set Comprehension

from wsgiref.validate import validator


produto = {
    'nome': 'Mouse',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

print(dc)