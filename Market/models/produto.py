from utils.helper import coin_float_to_str

class Produto:
    count: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.count
        self.nome: str = nome
        self.preco: float = preco
        Produto.count += 1

    @property
    def codigo(self: object) -> str:
        return self.__codigo

    def __str__(self: object) -> str:
        return (f'Código: {self.codigo}\n'
                f'Nome: {self.nome}\n'
                f'Preço: {coin_float_to_str(self.preco)}')
