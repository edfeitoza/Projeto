# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

#Criando a função

# def generator(n=0):
#     yield 1     #pausar
#     print('Continuando ...')
#     yield 2     #pausar
#     print('Mais uma vez ...')
#     yield 3     #pausar
#     print('Terminou')

# gen = generator(n=0)    #executando a função

# for n in gen:
#     print(n)

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n > maximum:
            return

gen = generator(n=0, maximum=20)    #executando a função

for n in gen:
    print(n)