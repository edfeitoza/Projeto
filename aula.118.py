#Problemas dos parametros mutaveis em funções Python

def adiciona_clientes(nome, lista=None):         #Forma correta de criar lista em uma função
    if lista is None:                            #Enquanto a lista for None o Python criará uma lista nova   
        lista = []
    lista.append(nome)
    return lista


clientes1=adiciona_clientes('Programacao')
adiciona_clientes('Python', clientes1)
adiciona_clientes('PHP', clientes1)
adiciona_clientes('COBOL', clientes1)

clientes2=adiciona_clientes('Jundiai')
adiciona_clientes('Varzea', clientes2)
adiciona_clientes('Campo Limpo', clientes2)
adiciona_clientes('Jarinu', clientes2)




print(clientes1)
print(clientes2)
