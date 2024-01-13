# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# lista = []
# for x in range(5):
#     for y in range(5):
#         lista.append((x,y))
# print(lista)


#List comprehension

lista = [
    (x,y)
    for x in range(5)
    for y in range(5)
]

print(lista)