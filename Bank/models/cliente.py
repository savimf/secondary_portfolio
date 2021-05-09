from datetime import date
from utils.helper import date_to_str, str_to_date


class Cliente:
    count: int = 1

    def __init__(self: object, nome: str, cpf: str, data_nasc: str) -> None:
        self.__codigo: int = Cliente.count
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_nasc: date = str_to_date(data_nasc)
        self.__data_cad: date = date.today()
        Cliente.count += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nasc(self: object) -> str:
        """Recebe a data de nascimento no formato date
        e a retorna no formato 'dd/mm/aaaa'.

        Args:
            self (object): objeto.

        Returns:
            str: 'dd/mm/aaaa'.
        """
        return date_to_str(self.__data_nasc)

    @property
    def data_cad(self: object) -> str:
        """Recebe a data de cadastro no formato date
        e a retorna no formato 'dd/mm/aaaa'.

        Args:
            self (object): objeto.

        Returns:
            str: 'dd/mm/aaaa'.
        """
        return date_to_str(self.__data_cad)

    def __str__(self: object) -> str:
        return (f'Código: {self.codigo}\n'
                f'Nome: {self.nome}\n'
                f'CPF: {self.cpf}\n'
                f'Data de nascimento: {self.data_nasc}\n'
                f'Data de cadastro: {self.data_cad}')
