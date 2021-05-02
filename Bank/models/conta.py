from models.cliente import Cliente
from utils.helper import coin_float_to_str

class Conta:
    codigo: int = 100

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.
        self.__limite: float = 100.
        self.__saldo_total: float = self._calc_saldo_total
        Conta.codigo += 1


    @property
    def numero(self: object) -> int:
        return self.__numero


    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente


    @property
    def saldo(self: object) -> float:
        return self.__saldo


    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor


    @property
    def limite(self: object) -> float:
        return self.__limite


    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor


    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total


    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor


    def __str__(self: object) -> str:
        return (f'Número da conta: {self.numero}\n'
                f'Cliente: {self.cliente.nome}\n'
                f'Saldo total: {coin_float_to_str(self.saldo_total)}')


    @property
    def _calc_saldo_total(self: object) -> float:
        return self.saldo + self.limite


    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calc_saldo_total

            print('Operação realizada com sucesso.')
        else:
            print('Valor inválido.')


    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.limite -= (valor - self.saldo)
                self.saldo = 0

            self.saldo_total = self._calc_saldo_total

            print('Operação realizada com sucesso.')
        else:
            print('Falha ao realizar saque. Favor verificar valor e saldo.')


    def transferir(self: object, destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.limite -= (valor - self.saldo)
                self.saldo = 0

            self.saldo_total = self._calc_saldo_total
            destino.saldo += valor
            destino.saldo_total = destino._calc_saldo_total

            print('Operação realizada com sucesso.')
        else:
            print('Falha ao realizar transferência. Favor verificar valor e saldo.')
