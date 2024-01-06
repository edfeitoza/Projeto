"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudo(nome):
        return f"{saudacao}, {nome}!!"

    return saudo


saudar = criar_saudacao("Bastarde")
saudar1 = criar_saudacao("Basnoite")


nome = input("Informe o seu nome: ")
print(saudar(nome))
print(saudar1(nome))
