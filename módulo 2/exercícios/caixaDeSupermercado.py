import os
os.system('clear')

produtos = {
    'Arroz': 5.60,
    'Feijão': 4.50,
    'Macarrão': 2.75,
    'Leite': 7,
    'Ovos': 15.30,
}

print('--- SISTEMA CAIXA ---')
for produto, preco in produtos.items():
    print(f'{produto} --- R$ {preco:.2f}')

def total(*args):
    return sum(args)

carrinho_itens = []

while True:
    carrinho_produto = input('Informe os produtos que deseja (ou digite "finalizar"): ').strip()

    if carrinho_produto.lower() == 'finalizar':
        break

    if carrinho_produto in produtos:
        carrinho_itens.append(carrinho_produto)
        print('Item adicionado com sucesso!')
    else:
        print('Produto não encontrado! Tente novamente.')

    print('Seu carrinho:')
    for carrinho in carrinho_itens:
        print(f'- {carrinho}')

preco_itens = [produtos[produto] for produto in carrinho_itens]
soma = total(*preco_itens)

os.system('clear')
print('--- NOTA FISCAL ---')
print('     PRODUTOS      ')
for produto in carrinho_itens:
    print(f'{produto}: R$ {produtos[produto]:.2f}')
print(f'\nTotal a pagar: R$ {soma:.2f}')
