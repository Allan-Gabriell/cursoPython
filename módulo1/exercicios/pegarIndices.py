'''
Exercícios
Exibas os índices da lista
'''
import os

os.system('clear')
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome)