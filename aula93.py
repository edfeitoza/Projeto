#Try, except, else e finally

#Tratativas de erros em códigos
#Deve-se informar a excessão para a tratativa, caso seja necessário é possivel tratar mais de uma exceção except(TypeError, IndexError):


try:
    a = 10
    b = 0
    c = a/b
    print(f'total é: ',c)

except ZeroDivisionError as error:                     
    print('Não existe divisão por ZERO!!', error)
    print('Nome: ', error.__class__.__name__)
