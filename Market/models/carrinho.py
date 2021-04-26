from models.produto import Produto
from time import sleep

class Carrinho:
    itens: dict = {}


    @classmethod
    def __len__(cls) -> int:
        return len(cls.itens)


    @classmethod
    def _add_item(cls, p: Produto) -> None:
        if p in cls.itens.keys():
            cls.itens[p] += 1
        else:
            cls.itens[p] = 1

        print(f'Produto adicionado. {cls.itens[p]} ' + \
            'unidade(s) no carrinho.')


    @classmethod
    def _rm_item(cls, p: Produto) -> None:
        if p in cls.itens.keys():
            del cls.itens[p]
            print('Produto removido com sucesso.')
        else:
            print('Produto não consta no carrinho.')


    @classmethod
    def visualizar(cls) -> None:
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
        cls.itens.clear()


    @classmethod
    def valor(cls) -> float:
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
