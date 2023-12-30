#Exercicio

nome = 'Edilson'
altura = 1.73
peso = 100
IMC = ...

IMC = peso/(altura**2)

#print(nome, ' tem ', altura, ' de altura ' , 'e pesa ', peso, 'quilos e seu IMC é', IMC)

#f-strings => formatando strings
linha_1 = f'{nome} tem {altura:.2f} de altura com {peso} quilos, portanto seu IMC é {IMC:.2f}'
print(linha_1)
