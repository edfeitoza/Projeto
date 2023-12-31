'''
Interpolação básica de strings
s - string (%s)
d e i - int (%d / %i)
f - float (%f)
x e X - hexadecimal (ABCDEF0123456789)

'''

nome = 'python'
preco = 1000.23
variavel = '%s, o valor é R$ %.2f' % (nome, preco)
print(variavel)
print(20*'-')
print('Valor hexadecimal de %d => %04X' % (1500, 1500))