#exemplo de uso dos SETs

letras = set()
while True:
    letra = input('Informe uma letra: ')
    letras.add(letra)
    
    if 'l' in letras:
        print(f'letra encontrada', letra)
        print(f'tentativas',letras)
        break
        