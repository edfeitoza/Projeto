# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

#Exemplo de Classe

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Python', 'Programacao')
p2 = Pessoa('Delphi', 'Pascal')

# p1 = Pessoa()
# p1.nome ='Python'
# p1.sobrenome ='Programacao'

# p2 = Pessoa()
# p2.nome = 'Delphi'
# p2.sobrenome = 'Pascal'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)