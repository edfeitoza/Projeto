from encodings import utf_8
import json

# pessoa = {
#     'nome': 'Python',
#     'sobrenome': 'Programacao',
#     'enderecos': [
#         {'rua': 'R1','numero': 32},
#         {'rua': 'R2','numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         ensure_ascii=False,      #Exibe os caracteres especiais no arquivo json
#         indent=2,                #Insere identação no arquivo   
#         )

#Importanto Json

with open('aula117.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))