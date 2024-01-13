#Dicionario - Pessoa
# pessoa = {
#     'nome': 'Python',
#     'sobrenome': 'Programação',
# }

#Dicionario dados_pessoa
# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# dados_completos = {
#     **pessoa, **dados_pessoa    #Desempacotamento de dicionários
# }
#Desempacotamento de dicionario

# a,b = pessoa.values()
# a,b = pessoa.items()
# print(a,b)

#Desempacotamento interno
# (a1, a2),(b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave,valor)

# print(pessoa, dados_pessoa)
# print(dados_completos)

#args e kwargs
#args
#kwargs - keyword arguments (argumentos nomeados)

# def mostro_argumentos_nomeados(*args, **kwargs):
#     print(kwargs)

# mostro_argumentos_nomeados(nome='Windows', idade= 30)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Windows', idade= 30)