import importlib        #Esse importa possibilita recarregar um módulo já carregado

import aula98_m

print(aula98_m.var)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print(10*'-')
print('Fim')