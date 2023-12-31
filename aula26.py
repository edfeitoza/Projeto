'''
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
< - direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flag - !r !s !a

'''

variavel = 'ABC'
numero = 1000.35789023

print(f'{variavel}')
print(f'{variavel:*>13}')
print(f'{variavel:*<13}')
print(f'{variavel:*^13}')

print(f'{numero:.2f}')

print(f'O hexadecimal de 1500 é {1500:08x}')