frase = ' O Python é uma linguagem de programação multiparadigma.' \
    ' Python foi criado por Guido van Rossum.'
    
#print(frase.count(''))

i = 0
qtd_letra_mais_vezes = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_letra_mais_vezes_atual = frase.count(letra_atual)
    
    if qtd_letra_mais_vezes < qtd_letra_mais_vezes_atual:
        qtd_letra_mais_vezes = qtd_letra_mais_vezes_atual
        qtd_letra_mais_vezes = letra_atual
    i += 1
    
    print( 'A letra que apareceu mais vezes foi '
    f'"{qtd_letra_mais_vezes}" que apareceu '
    f'{qtd_letra_mais_vezes}x'
    
    
    )