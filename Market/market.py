"""
MERCADO

Aplicação onde, ao ser inicializada, apresentará ao usuário um menu contendo
as opções:

i) cadastrar produto;
ii) listar produtos;
iii) comprar produtos;
iv) visualizar carrinho;
v) sair da aplicação.

Quando um produto já existente no carrinho for readicionado, sua quantidade
somente será atualizada, tal que o mesmo não será duplicado.

Ao finalizar a compra, será apresentado ao usuário o total da mesma de acordo
com as quantidades inseridas.
"""
from models.produto import Produto
from models.carrinho import Carrinho
from utils.helper import coin_float_to_str
from time import sleep

# lista para armazenamento dos produtos
produtos: list = []

# objeto do tipo carrinho (ver classe Carrinho)
carrinho: Carrinho = Carrinho()


def main() -> None:
    """Função principal, responsável pela execução do programa."""
    menu()


def menu() -> None:
    """Função responsável pela exibição do menu e execução das opções."""

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

    opcao: int = int(input('Opção: '))

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
    """Função responsável pelo cadastramento de um produto. Solicita ao
    usuário as informações do mesmo, como nome e preço, e o adiciona à
    lista 'produtos'."""

    print('Cadastro de produto\n'
          '===================')

    produto: Produto = Produto(
        input('Nome do produto: '),
        float(input('Preço: '))
    )

    produtos.append(produto)

    print(f'Produto {produto.nome} adicionado com sucesso.')
    sleep(1)
    menu()


def listar_produtos() -> None:
    """Função responsável pela listagem de produtos. Só é executada, porém,
    se há elementos na lista 'produtos'."""

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
    """Função responsável pela compra de um produto incluído na lista
    'produtos'. Só é executada se len(produtos) > 0. Uma vez executada,
    solicita ao usuário o código do produto e, se for encontrado, este
    será adicionado ao carrinho."""

    if len(produtos) > 0:
        print('====== Produtos Disponíveis ======')

        for produto in produtos:
            print(f'{produto}\n'
                  '----------------------------------')
            sleep(.5)

        codigo: int = int(input('Informe o código do produto a ser ' +
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
    """Função responsável pela remoção de um produto da lista 'produtos'.
    Só é executada se len(produtos) > 0. Uma vez executada, solicita ao
    usuário o código do produto e, se for encontrado, este será removido
    do carrinho."""

    if len(produtos) > 0:
        print('====== Produtos Disponíveis ======')

        for produto in produtos:
            print(f'{produto}\n'
                  '----------------------------------')
            sleep(.5)

        codigo: int = int(input('Informe o código do produto a ser ' +
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
    """Chama o método visualizar() da classe Carrinho."""

    Carrinho.visualizar()
    sleep(1)
    menu()


def fechar_pedido() -> None:
    """Função responsável pelo fechamento do pedido através do método
    .valor() da classe Carrinho. O valor da fatura será exibido no
    formato R$ xxxx.xx e posteriormente o Carrinho será esvaziado."""

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
    """Recebe um inteiro correspondendo ao código de um produto
    e, caso o mesmo conste na lista 'produtos', será retornado.
    Caso contrário, não há retorno.

    Args:
        codigo (int): código do produto a ser encontrado.

    Returns:
        Produto: produto da lista 'produtos' cujo código corresponda
        ao código informado. Caso não haja correspondência: return None.
    """

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
