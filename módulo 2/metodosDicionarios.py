# Métodos úteis dos dicionários em Python
# * len - quantas chaves
# * keys - interável com as chaves
# * values - interável com os valores
# * items - interável com chaves e valores
# * setdefault - adiciona valor se a chave não existe
# * copy - retorna uma cópia rasa (shallow copy)
# * get - obtém uma chave
# * pop - apaga um item com a chave especificada (del)
# * popitem - apaga o último item adicionado
# * update - atualiza um dicionário com outro

pessoa = {
    'nome': 'Allan',
    'sobrenome': 'Gabriel',
}

# informa a quantidade de elementos que tem no meu dicionário
# print(pessoa.__len__()) 

# Melhor usar essa outra forma
print(len(pessoa))
#uso para ver as chaves
print(pessoa.keys())
# posso tranformar numa lista ou tupla
print(list(pessoa.keys()))
# uso para ver os itens das chaves
print(tuple(pessoa.values()))