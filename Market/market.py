"""
MERCADO

Aplicação onde, ao ser inicializada, apresentará ao usuário um menu contendo
as opções:

i) cadastrar produto;
ii) listar produtos;
iii) comprar produtos;
iv) visualizar carrinho;
v) sair da aplicação;

Quando um produto já existente no carrinho for readicionado, sua quantidade
somente será atualizada, tal que o mesmo não será duplicado.

Ao finalizar a compra, será apresentado ao usuário o total da mesma de acordo
com as quantidades inseridas.
"""
from time import sleep
from models.produto import Produto
from utils.helper import coin_float_to_str

produtos: list = []
carrinho: dict = {}


def main() -> None:
    menu()


def menu() -> None:
    print('==================\n'
          '== Bem-vindo(a) ==\n'
          '==   Savi Shop  ==\n'
          '==================')

    print('Seleciona uma das opções abaixo: \n'
          '1 - Cadastrar produto\n'
          '2 - Listar produtos\n'
          '3 - Comprar produto\n'
          '4 - Visualizar carrinho\n'
          '5 - Fechar pedido\n'
          '6 - Sair')

    opcao: int = int(input())

    if opcao in range(1, 6):
        opcoes.get(opcao)()
    elif opcao == 6:
        print('Obrigado!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida.')
        sleep(.5)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto\n'
          '===================')

    nome: str = input('Nome do produto: ')
    preco: float = float(input('Preço: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'Produto {produto.nome} adicionado com sucesso.')
    sleep(1)
    menu()



def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos\n'
              '--------------------')

        for produto in produtos:
            print(f'{produto}\n'
                  '--------------------')
            sleep(.5)
    else:
        print('Ainda não há produtos cadastrados.')
    sleep(1)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('====== Produtos Disponíveis ======')

        for produto in produtos:
            print(f'{produto}\n'
                  '----------------------------------')
            sleep(.5)

        codigo: int = int(input('Informe o código do produto a ser' + \
            'adicionado ao carrinho: '))

        produto: Produto = pegar_prod_por_codigo(codigo)

        if produto:
            if produto in carrinho.keys():
                carrinho[produto] += 1
            else:
                carrinho[produto] = 1

            print(f'Produto adicionado. {carrinho[produto]} ' + \
                    'unidade(s) no carrinho.')
            sleep(1)
            menu()
        else:
            print('Produto não encontrado.')
            sleep(1)
            menu()

    else:
        print('Ainda não há produtos à venda.')
    sleep(1)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho.')

        for produto in carrinho.keys():
            print(f'{produto.nome}\n'
                  f'Quantidade: {carrinho.get(produto)}\n'
                  '----------------------------------')
            sleep(1)
    else:
        print('Ainda não há produtos no carrinho.')
    sleep(1)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')

        for item in carrinho.items():
            print(f'{item[0]}\n'
                  f'Quantidade: {item[1]}')

            valor_total += item[0].preco * item[1]
            print('------------------')
            sleep(1)

        print(f'Sua fatura é de {coin_float_to_str(valor_total)}\n'
              'Volte sempre!')

        carrinho.clear()
        sleep(3)
    else:
        print('Ainda não há produtos no carrinho.')
    sleep(1)
    menu()


def pegar_prod_por_codigo(codigo: int) -> Produto:
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None

opcoes: dict = {1: cadastrar_produto,
                2: listar_produtos,
                3: comprar_produto,
                4: visualizar_carrinho,
                5: fechar_pedido}

if __name__ == '__main__':
    main()
