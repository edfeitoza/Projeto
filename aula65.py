"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada / não valor).
"""
def soma(var1,var2):
    int_var1 = int(var1)
    int_var2 = int(var2)
    total = (int_var1 + int_var2)
    print(f'O primeiro valor digitado foi: {var1}, o segundo valor digitado foi: {var2}')
    print(f'O total é: ', total)

a = input('Informe o primeiro valor: ')
b = input('Informe o segundo valor: ')
soma(a,b)

