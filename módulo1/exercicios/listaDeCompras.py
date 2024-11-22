'''
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de inserir, apagar e listar
valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes
na lista
'''
import os

os.system('clear')

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
           indice = int(indice_str)
           del lista[indice]
        except ValueError:
            print('Por favor digite um int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Error desconhecido')
    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
            print("Nada para listar")
        
        for i, valor in enumerate(lista):
            print(i, valor)