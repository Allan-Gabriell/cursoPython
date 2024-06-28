'''
Dessa forma fazemos a formatação de estrings em python
'''
nome = 'Allan'
altura = 1.80

linha_1 = 'O nome tem altura de altura'
print(linha_1)

# f-strings
linha_2 = f'O {nome} tem {altura:.2f} de altura'
print(linha_2)

'''
Outra forma é usar a função format
'''
a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f} '.format(a, b, c)

print(formato)