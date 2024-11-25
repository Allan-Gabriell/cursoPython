import os
os.system('clear')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

for numero in [2, 3, 4, 5, 6, 7, 8, 9]:
    print(duplicar(numero))
    print(triplicar(numero))
    print(quadruplicar(numero))
    print('--------------------')