nomes = ['Maria', 'Helena', 'Luiz']

nomes_enumerado = list(enumerate(nomes))
print(nomes_enumerado)
print(10*'-')
for item in enumerate(nomes):
    print (item)
print(10*'-')
for indice, nome in enumerate(nomes):
    print(indice, nome)
print(10*'-')
