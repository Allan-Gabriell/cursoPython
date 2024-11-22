'''
Introdução ao desempacotamento + tuples (tuplas)
'''
import os

os.system('clear')
nomes = ['Maria', 'Helena', 'Luiz'] # Uma lista é como um pacote
nome1, nome2, nome3 = nomes #preciso ter o mesmo total de valores e variáveis
print(nome1)

print('--------------------------------')
#Pegar somente um valor
nome4, *resto = nomes
print(nome4, resto)

print('--------------------------------')
#Não é muito interessante criar uma variável que não vai ser usado
# por isso é melhor usar o seguinte
_, nome4, *_ = nomes # O _ significa que eu tô pulando um valor
print(nome4)

print('--------------------------------')
"""
Tipo tupla - uma lista imutável

é só eu tirar os [] ou colocar ()
"""
nomes = ('Maria', 'Helena', 'Luiz')
_, _, nome4, *_ = nomes 
print(nome4, nomes)