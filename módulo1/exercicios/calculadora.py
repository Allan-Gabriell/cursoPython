"""Calculadora com while"""

print("Calculado com While")

while True:
    num1 = float(input('Informe um número: '))
    num2 = float(input('Informe outro número: '))
    #####
    operador = input('Informe o operador ( + - * / ): ')
    #####
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado == num1 * num2
    elif operador == '/':
        resultado == num1 / num2
    else:
        print('Não foi informado um operador válido!')
    #####
    print(f'O resultado da operação {num1} {operador} {num2} é {resultado}')
    #####
    sair = input('Deseja sair? ').lower()
    if sair == 'sair' or sair.startswith('s'):
        print("Fim!")
        break