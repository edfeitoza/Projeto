# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# https://www.youtube.com/watch?v=-3HJcQMWv7Y
# & D:\Program1\Python311\Scripts\black.exe .\aula72.py

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multi1 = multiplica(2, 2, 2, 4)
print(multi1)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def parimpar(x):
    if x % 2:
        print(f"O valor informado {x}, é impar!!")
    else:
        print(f"O valor informado {x}, é par!!")


num1 = int(input("Informe um valor para checar se é impar ou par: "))

parimpar(num1)
