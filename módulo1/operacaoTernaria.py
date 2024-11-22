'''
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''
import os
os.system('clear')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito #mesma coisa da linha anterior
print(novo_digito)