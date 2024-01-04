'''
Operação ternária (Condicional de uma linha)
<valor> if <condição> else <outro valor>


########################################
condicao = 12 == 12
var1 = 'Se IF for TRUE' if condicao else 'Se IF  for FALSE'
print(var1)
'''
digito = input('informe o valor: ')
int_digito = int(digito)

novo_digito = int_digito if int_digito <= 9 else 0
print(novo_digito)
