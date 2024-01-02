while True:
    num1 = input('Informe um valor inteiro: ')
    num2 = input('Informe outro valor inteiro: ')
    op = input ('Informe a operação desejada: "+ - / *" ')
    
    #flag de checagem
    num_validos = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True          #Se num1 e num2 foram válidos, retorna "true" caso contrário "false"
    except:
        num_validos = None
    
    if num_validos is None:
        print('Valores incorretos, tente novamente!')
        continue
    
    op_validos = '+-/*'
    
    if op not in op_validos:
        print('Operador não é válido, tenta novamente!')
        continue
    if len(op) > 1:
        print('Informe apenas um operador, tenta novamente!')
        continue
    print('Realizando calculo. Confira o resultado: ')
    
    if op == '+':
        print(f'{num1_float} + {num2_float}=', num1_float + num2_float)
    elif op == '-':
        print(f'{num1_float} - {num2_float}=', num1_float - num2_float)
    elif op == '*':
        print(f'{num1_float} * {num2_float}=', num1_float * num2_float)
    elif op == '/':
        print(f'{num1_float} / {num2_float}=', num1_float / num2_float)
    else:
        print('divisão por 0')
    
    sair = input('Deseja sair? [s]im [n]ão: ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break

