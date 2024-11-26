'''
Manipulando chaves e valores em dicionários
'''
import os
os.system('clear')

pessoa = {}

chave = 'nome' #criei uma chave dinâmica

pessoa[chave] = 'Allan Gabriel'
pessoa['sobrenome'] = 'Freitas'

print(pessoa[chave])
print(pessoa)

del pessoa['sobrenome']
print(pessoa)

# print(pessoa.get('sobrenome', 'Não existe')) #Por padrão se a chave não existir ele retorna none
if pessoa.get('sobrenome') is None:
    print('Não Existe!')
else:
    print(pessoa['sobrenome'])
# print(pessoa['nome1'])