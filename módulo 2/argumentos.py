'''
Agumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
import os
os.system('clear')

'''
Parâmetro = nome da variável
Argumento = o valor que eu passo para elas
'''

#argumento não nomeado ou posicional
def soma(x,y):
    #definição da função
    print(x+y)

soma(1, 2) #posicional por que a ordem como passo meus argumentos importam
#argumentos nomeados
soma(y=2, x=1)