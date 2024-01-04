#Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'python','é','legal'
salas = [
    
    ['Maria', 'Helena', ],
    
    ['Elaine', ],
    
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)],
]

a,b,*_,u = lista
print(a,b,u)

print(10*'-')

for nome in lista:
    print(nome)

print(10*'-')

print(*lista)
print(*string)
print(*tupla)

print(10*'-')

print(*salas, sep='\n')


#for nome in lista:
#    print(nome, end=' ')

