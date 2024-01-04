"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = ' Olha só que , coisa interessante '
print(10*'-')
lista_palavras = frase.split()
print(lista_palavras)
print(10*'-')
lista_frase = frase.split(',')
print(lista_frase)
print(10*'-')

for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip())
print(lista_frase)