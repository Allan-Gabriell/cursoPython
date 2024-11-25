'''
Dicionário em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de 'chaves' e 'valor'
Chaves podem ser consideradas como o 'índice' que vimos na lista
e podem ser de tipos imutáveis como: str, int float, bool, trupe, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usamos as chaves - {} - ou a classe dict para criar dicionários
Imutáveis: str, int, float, bool, trupe
mutáveis: dict, list
pessoa = {
    'nome': 'Allan',
    'sobrenome': 'Gabriel',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': '...', 'número': 123},
        {{'rua': '...', 'número': 321}
    ]
}
'''
import os
os.system('clear')

# pessoa = dict(nome='Allan')
pessoa = {
    'nome': 'Allan',
    'sobrenome': 'Gabriel',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': '...', 'número': 123},
        {'rua': '...', 'número': 321}
    ]
}
print(pessoa, type(pessoa))
print(pessoa['nome'])
print('-----------------------')

for chave in pessoa:
    print(chave, pessoa[chave])