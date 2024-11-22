'''
Desempacotando em chamadas de métodos e funções
'''
import os
os.system('clear')

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, *_, c = lista
# print(a, c)

print(*lista) #percorre todos os elementos da lista separando cada elemento por espaço
print(*string)
print(*tupla)