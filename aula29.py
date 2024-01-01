'''
Introdução ao try/except

try => tentar executar o código
except => ocorreu algum erro ao executar o código
'''

numero_str = input('Informe um valor: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um numero válido!')