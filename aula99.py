# from sys import path

# # print(path, sep='\ n')
# import aula99_package.modulo

# # from aula99_package.modulo import soma_do_modulo

# # print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 4))

##########################################################################################
# from aula99_package import modulo as md         #é a melhor forma de importar modulo
# print(md.soma_do_modulo(2,2))

# print(__name__)

import aula99_package

print(aula99_package.soma_do_modulo(2,3))