from models.produto import Produto
from time import sleep


class Carrinho:

    # dicionário para armazenar os itens do carrinho;
    # as chaves serão os produtos e os valores suas quantidades.
    itens: dict = {}

    @classmethod
    def __len__(cls) -> int:
        return len(cls.itens)

    @classmethod
    def _add_item(cls, p: Produto) -> None:
        """Adiciona o produto p ao dicionário 'itens'. Se p
        já estiver presente em 'itens', seu valor será acres-
        cido de 1, caso não esteja, seu valor será setado a 1.

        Args:
            p (Produto): produto a ser adicionado a 'itens'.
        """
        if p in cls.itens.keys():
            cls.itens[p] += 1
        else:
            cls.itens[p] = 1

        print(f'Produto adicionado. {cls.itens[p]} ' +
              'unidade(s) no carrinho.')

    @classmethod
    def _rm_item(cls, p: Produto) -> None:
        """Remove o produto 'p' do dicionário 'itens', se
        este constar no mesmo.

        Args:
            p (Produto): produto a ser removido.
        """
        if p in cls.itens.keys():
            del cls.itens[p]
            print('Produto removido com sucesso.')
        else:
            print('Produto não consta no carrinho.')

    @classmethod
    def visualizar(cls) -> None:
        """Se len(cls.itens) > 0, percorrerá cada produto
        do mesmo e mostrará seu nome e a quantidade presen-
        te.
        """
        if len(cls.itens) > 0:
            print('== Produtos no carrinho ==')

            for produto in cls.itens.keys():
                print(f'{produto.nome}\n'
                      f'Quantidade: {cls.itens.get(produto)}\n'
                      '----------------------------------')
                sleep(.5)
        else:
            print('Ainda não há produtos no carrinho.')

    @classmethod
    def _esvaziar(cls) -> None:
        """Realize o método .clear() sobre cls.itens."""
        cls.itens.clear()

    @classmethod
    def valor(cls) -> float:
        """Se len(cls.itens) > 0, percorrerá todos os
        produtos contidos no mesmo e somará o valor cor-
        respondente de cada produto ao valor total do
        carrinho, inicialmente setado como 0.

        Returns:
            float: valor total da compra.
        """
        if len(cls.itens) > 0:
            valor_total: float = 0

            print('== Produtos do carrinho ==')

            for item in cls.itens.items():
                print(f'{item[0]}\n'
                      f'Quantidade: {item[1]}')

                valor_total += item[0].preco * item[1]
                print('------------------')
            return valor_total
        return 0
