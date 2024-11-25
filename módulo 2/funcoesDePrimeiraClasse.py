'''
Higher Order Functions
Funções de primeira Classe
Funções em Python é um tipo de dado que podemos manipular da forma
que queremos

- Higher Order Functions - Funções que podem receber e/ou retornar outras funções
- First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
'''
import os 
os.system('clear')

def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

v = executa(saudacao, 'Bom dia')
print(v)