#isinstance = serve para saber se o objeto é de um determinado tipo

from turtle import st


lista = [
    'a','w', 1, 1.1,True,[0,1,2,3],(1,2),
    {0,1}, {'nome': 'Luiz'}
]
#Checando se tenho um SET na lista

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(10)
        print(item, isinstance(item,set))
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))
        
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    
    else:
        print('Outros')
        print(item)