
'''
cont = 0

while cont < 10:
    cont += 1
    print(cont*'-', cont)
    if cont == 4:
        break

'''

cont = 0

while cont < 70:
    cont += 1
    
    if cont == 40:
        continue
    
    if cont >= 10 and cont <=20:
        continue
    
    print(cont*'|', cont)