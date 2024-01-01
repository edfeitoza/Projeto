num1 = input('Informe um numero inteiro: ')

try:
    num_int = int(num1)
    modulo = num_int % 2 == 0
    if modulo:
        print(f'O {num_int} é um valor par')
    else:
        print(f'O {num_int} é um valor impar')
except:
    print('Isso não é um numero válido!')