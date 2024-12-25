# Função lambda em python
# A função lambda é uma função como qualquer outra em
# pyhton. Porém, são funções anônimas que contém apenas
# uma linha. Ou seja, tudo deve ser contido dentro de uma
# unica expressão.

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]

# def ordena(item):
#     return item['nome']

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)