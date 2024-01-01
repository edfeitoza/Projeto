
nome = input('informa seu nome: ')
idade = input('informe sua idade: ')

print(nome,idade)
#nome_invertido = nome[::-1]
nome_caracteres = len(nome)
nome_uletra = nome[0:1]
nome_pletra = nome[-1:]


if nome and idade:
    print(f'o seu nome é %s e sua idade %s anos' % (nome, idade))
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contém espaços')
    
    print(f'O seu nome invertido é {nome[::-1]}')
    print(f'O seu nome possui {len(nome)} caracteres')
    print(f'A primeira letra do seu nome {nome[0]}')
    print(f'A ultima letra do seu nome {nome[-1]}')



else:
    print('Campo requerido em branco!!!')

'''
nome_pletra = nome[-1:]
print(nome_pletra)

nome = 'noslidE'
nome_uletra = nome[0:1]
nome_pletra = nome[-1:]

print(nome_uletra)
print(nome_pletra)
'''
