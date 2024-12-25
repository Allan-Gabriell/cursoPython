# list comprehension em python
# é uma fomr mais rápida de criar listas a partir de interáveis

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

print('-----------------------------------')

# Agora utilizando list comprehension
lista = [numero for numero in range(10)]
print(lista)

# Posso fazer operações dentro da list comprehension

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)