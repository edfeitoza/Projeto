'''
Operadores Lógicos
and / or / not

and => todas as condições precisam ser verdadeiras (true)
or => basta apenas uma condição para ser verdadeira (true)
not => todas as condições precisam ser falsas (false)

Falsy => 0 / 0.0 / '' - considerados falsos
none => não valor

menu = input('[E]ntrar [S]air: ')
senha_informada = input('informe a senha: ')
senha_permitida = 'senha'

if menu == 'E' and senha_informada == senha_permitida:
    print('Senha correta!')
else:
    print('Dados invalidos')
    
'''

menu = input('[E]ntrar [S]air: ')
senha_informada = input('informe a senha: ')
senha_permitida = 'senha'

if (menu == 'E' or menu == 'e') and senha_informada == senha_permitida:
    print('Senha correta!')
else:
    print('Dados invalidos')
