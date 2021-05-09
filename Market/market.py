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
from models.produto import Produto
from models.carrinho import Carrinho
from utils.helper import coin_float_to_str
from time import sleep

produtos: list = []
carrinho: Carrinho = Carrinho()


def main() -> None:
    menu()


def menu() -> None:
    print('==================\n'
          '== Bem-vindo(a) ==\n'
          '==   Savi Shop  ==\n'
          '==================')

    print('Selecione uma das opções abaixo: \n'
          '1 - Cadastrar produto\n'
          '2 - Listar produtos\n'
          '3 - Comprar produto\n'
          '4 - Remover produto\n'
          '5 - Visualizar carrinho\n'
          '6 - Fechar pedido\n'
          '7 - Sair')

    opcao: int = int(input())

    if opcao in range(1, 7):
        opcoes.get(opcao)()
    elif opcao == 7:
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
    sleep(.5)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('====== Produtos Disponíveis ======')

        for produto in produtos:
            print(f'{produto}\n'
                  '----------------------------------')
            sleep(.5)

        codigo: int = int(input('Informe o código do produto a ser ' + \
            'adicionado ao carrinho: '))

        produto: Produto = __pegar_prod_por_codigo(codigo)

        if produto:
            Carrinho._add_item(produto)
            sleep(.5)
        else:
            print('Produto não encontrado.')
    else:
        print('Ainda não há produtos à venda.')

    sleep(1)
    menu()


def remover_produto() -> None:
    if len(produtos) > 0:
        print('====== Produtos Disponíveis ======')

        for produto in produtos:
            print(f'{produto}\n'
                  '----------------------------------')
            sleep(.5)

        codigo: int = int(input('Informe o código do produto a ser ' + \
            'removido do carrinho: '))

        produto: Produto = __pegar_prod_por_codigo(codigo)

        if produto:
            Carrinho._rm_item(produto)
            sleep(.5)
        else:
            print('Produto não encontrado.')
    else:
        print('Ainda não há produtos à venda.')
    sleep(1)
    menu()


def visualizar_carrinho() -> None:
    Carrinho.visualizar()
    sleep(1)
    menu()


def fechar_pedido() -> None:
    valor = Carrinho.valor()

    if valor > 0:
        print(f'Sua fatura é de {coin_float_to_str(valor)}\n'
              'Volte sempre!')

        Carrinho._esvaziar()
    else:
        print('Ainda não há produtos no carrinho.')
    sleep(.5)
    menu()


def __pegar_prod_por_codigo(codigo: int) -> Produto:
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None


opcoes: dict = {1: cadastrar_produto,
                2: listar_produtos,
                3: comprar_produto,
                4: remover_produto,
                5: visualizar_carrinho,
                6: fechar_pedido}

if __name__ == '__main__':
    main()
