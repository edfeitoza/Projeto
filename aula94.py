#Try, except, else e finally

try:
    print('abre arquivo')
    #8/0
except ZeroDivisionError:
    print('Divisão por zero')
else:
    print('Sem problemas e sem erros!!')

finally:
    print('Terminou o código!!')