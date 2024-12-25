def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)

# ou  para o caso da soma

print(executa(
    lambda *args: sum(args),
    1, 2, 3, 4, 5, 6, 7
))

duplicar = executa(
    lambda multiplicador: lambda numero: numero * multiplicador,
    2
)

print(duplicar(5))