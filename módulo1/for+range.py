"""
For + Range
range -> range(start, stop, step)

funciona para os outros laços de repetição
"""

number = range(10) # Quando eu coloco somente um número eu defino o stop no número
print(number)
print(number[0])

number = range(5, 10)
print(number)

number = range(5, 10, 2) # Eu começo no 5 vou até o 10 e pulo de 2 em 2
print(number)

numbers = range(10)
for number in numbers:
    print(number)

numbers = range(5, 10)
for number in numbers:
    print(number)