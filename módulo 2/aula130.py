# Exemplo de uso dos sets
letras = set()

while True:
    letra = input('Informe uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabens')
        break

    print(letras)