'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF multiplicando cada um
dos valores por uma contagem regressiva começando de 10

EX.: 746.824.890-70
    10 9 8 7 6 5 4 3 2 
    7  4 6 8 2 4 8 9 0
    70 36 48 56 10 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301*10 = 3010
obter o resto da divisão da conta anteriro por 11
3010 % 11 = 7
se o resultado anteriro for maior que 9
    resultado é 0
contrário disso é:
    o resultado é o valor da conta

O primeiro dígito do CPF é 7
'''
import re
import os
import sys
os.system('clear')

# CPF_enviado_usuario = '746.824.890-70'.replace('.', '').replace('-', '')
# #replace substitui uma coisa por outra
# ou usamos o RE
entrada = input('Informe o CPF: ')
CPF_enviado_usuario = re.sub(r'[^0-9]', '', entrada)
# [^0-9] tudo de 0-9 que não é número

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados seuqenciais!')
    sys.exit()
    

nove_digitos = CPF_enviado_usuario[:9] # fiz um fatiamento até o 9
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

CPF_gerado = f'{nove_digitos}{digito_1}{digito_2}'
if CPF_enviado_usuario == CPF_gerado:
    print(f'{CPF_enviado_usuario} é válido!')
else:
    print('CPF inválido!')