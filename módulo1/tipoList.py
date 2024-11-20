"""
Listas em Python

Tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""

#lista = list() -> uma das formas de criar uma lista
# mas o mais comum é
import os

os.system('clear')
lista = []
print(lista, type(lista))
print('--------------------')
lista = [123, True, 'Allan', 1.2, []] # posso ter uma lista dentro da outra
print(lista)
print(lista[2].upper(), type(lista[2])) 
lista[2] = 'Allan Gabriel'
print(lista[2])
#upper() - coloca umas string em letras maiúsculas