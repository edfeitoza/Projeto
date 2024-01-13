
#transfomando função em função lambda de uma linha

def executa (funcao, *args):
    return funcao(*args)

# def soma(x,y):
#     return x + y

# #executando a função
# print(
    
#     executa(soma,2, 3)
# )

# print(
    
#     soma(2, 3)
# )

# # Essa função em Lambda

# print(
    
#     executa(
#         lambda x, y: x + y,
#         2, 3
#     ),
# )

###############################################################

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

 # Essa função em Lambda
 
duplica = executa(
    lambda m: lambda n: n * m,
    2
    
)

print(
    duplica(3)
)