# dir, hasattr e getattr em Python

string = 'Python'
metodo = 'lower'

if hasattr(string, metodo):
    print('metodo existente', metodo)
    print(getattr(string, metodo)())
else:
    print('Metodo não existente', metodo)