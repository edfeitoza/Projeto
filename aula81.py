# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [4,10,8,7,5,3,1,2,6,9, ]
# #lista.sort()  #ordena a lista original
# lista.sort(reverse=True) #ordena de forma inversa
# #sorted(lista) #faz uma cópia rasa da lista e ordena
# print(lista)

lista = [
    {'nome': 'Antonio', 'sobrenome': 'Elle'},
    {'nome': 'Cesar', 'sobrenome': 'Beraldo'},
    {'nome': 'Daniel', 'sobrenome': 'David'},
    {'nome': 'Benilson', 'sobrenome': 'Calvo'},
    {'nome': 'Elcio', 'sobrenome': 'Alves'},
]

# def ordena(item):
#     return item['nome']

#lista.sort(key=ordena)

# lista.sort(key=lambda item: item['nome']) #função lambda substitui a função acima comentada.

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)
    print()
    
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

