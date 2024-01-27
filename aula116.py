import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#Path para criar arquivos

caminho_arquivo= 'V:\\6-Python\\udemy\\ScriptsPython2\\ScriptsPython2\\pasta1\\'
caminho_arquivo += 'python.txt'

# arquivo = open(caminho_arquivo,'w')
# arquivo.close()

# with open(caminho_arquivo,'w') as arquivo:
#     print('Ola mundo!!')
#     print('Esse arquivo será fechado!!!')

# with open(caminho_arquivo,'w+') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.writelines(
#         ('linha 3\n', 'linha 4\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('### - lendo linha a alinha efeito next - ###')
#     arquivo.seek(0,0)                   #Mmovendo o cursor para o inicio do arquivo
#     print(arquivo.readline(), end='')   #Retira a quebra de linha
#     print(arquivo.readline().strip())   #Retira a quebra de linha
#     print(arquivo.readline().strip())   #Retira a quebra de linha
    
#     print('### - lendo linha a linha com FOR - ###')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
    
# print(20*'#')
# with open(caminho_arquivo,'r') as arquivo:
#     print(arquivo.read())
    
# with open(caminho_arquivo,'a+') as arquivo:     #inicia a escrita do arquivo a partir da ultima linha
#     arquivo.write('linha 5\n')
#     arquivo.write('linha 6\n')
#     arquivo.writelines(
#         ('linha 7\n', 'linha 8\n')
#     )

#Encoding 
with open(caminho_arquivo,'a+', encoding='utf-8') as arquivo:  #correção de acentuação - encoding
    arquivo.writelines(
        ('Atenção\n', 'Facão\n', 'Açougue\n','Malhação\n')
    )

#Removendo arquivo
#os.remove(caminho_arquivo)
#os.unlink(caminho_arquivo)

#Renomeia ou Move o arquivo
#os.rename(caminho_arquivo, 'novo-nome.txt')

