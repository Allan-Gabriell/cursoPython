'''
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o valor total e morte o valor

Crie uma função que fala se um número é par ou ímpar e retorne
'''
import os
os.system('clear')

def mult(*args):
    total = 1  
    for valor in args:
        total *= int(valor) 
    return total  

def impar_par(numero):
    if numero % 2 == 0:
        return 1
    else: 
        return 0 


valores = input('Informe os valores: ')
resultado = mult(*valores)
print(f'O resultado da multiplicação é {resultado}')
par_ou_impar = impar_par(resultado)
print('Par' if par_ou_impar == 1 else 'Impar')
