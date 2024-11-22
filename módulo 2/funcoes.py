'''
Introdução às funções (def) em python
Funções são trechos de código usads para replicar determinada
ação ao longo do código
Elas podem receber valores para parâmetros (argumentos) e retornar
um valor específico
Por padrão, funções python retornam None (nada)
'''
import os
os.system('clear')

def imprimir(a, b, c):
    print(a, b, c)

def saudacao(nome):
    print(f'Olá, {nome}! Tudo bem?')


saudacao('Allan')
imprimir(1, 2, 3)