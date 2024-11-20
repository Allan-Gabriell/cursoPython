'''
Métodos úteis para o tipo list:
    append, insert, pop, del, clear, extend, +
created read update  delete
Criar,  ler, alterar, apagar = lista[i] (CRUD)
'''
import os

os.system('clear')
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300

# del lista[2] # deleta o elemento selecionado
# print(lista)
# print(lista[2])

lista.append(100) # adiciona o elemento no fuim da lista
print(lista)

lista.pop() # Remove o último elemento da lista
print(lista)