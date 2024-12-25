# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# Processo de empacotamento
a, b = pessoa.values()
print(a, b)

print('-------------------------')

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# Processo de desempacotamento
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword argments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    print(kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(2024, 10, nome='joana', idade=16)