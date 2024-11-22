'''
args - Argumentos não nomeados
* _ *args (empacotamento e desempacotamento)
'''
import os
os.system('clear')

#Lembre-te de desempacotamento
x, y, *_ = 1, 2, 3, 4
print(x, y, _)
print('-------------------------')

# def soma(x,y):
#     return x + y

def soma(*args): #gera uma tupla e fiz o empacotamento
    total = 0
    print(args, type(args))
    for numero in args:
        total += int(numero)
    return total


numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros) #desempacotei
print(outra_soma)
print('------------------------------')
resultado = soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(resultado)