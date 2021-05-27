from datetime import date
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
        self._transacoes: list = [
            f'Data: {date.today()} - Conta de código {self.numero} criada.'
        ]

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
        """Retorna o saldo total da conta: soma do saldo
        com o limite.

        Args:
            self (object): objeto (conta).

        Returns:
            float: saldo + limite
        """
        return self.saldo + self.limite

    def _ext_saque(self: object, v: float) -> None:
        self._transacoes.append(
            f'Data: {date.today()} - Saque de '
            f'{coin_float_to_str(v)} realizado.'
        )

    def _ext_deposito(self: object, v: float) -> None:
        self._transacoes.append(
            f'Data: {date.today()} - Depósito de '
            f'{coin_float_to_str(v)} realizado.'
        )

    def _ext_transferencia(self: object,
                           c_destino: int,
                           v: float) -> None:

        self._transacoes.append(
            f'Data: {date.today()} - Transferência de '
            f'{coin_float_to_str(v)} realizada. '
            f'Num. conta de destino: {c_destino}'
        )

    def sacar(self: object, valor: float) -> None:
        """Dado saldo_total >= valor > 0, se saldo >=
        valor, decresce-o do mesmo e, caso contrário,
        decresce a diferença entre valor e saldo do
        limite, setando o saldo para 0. Por fim, atua-
        liza o saldo total.

        Args:
            self (object): objeto (conta).
            valor (float): valor a ser sacado.
        """
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.limite -= (valor - self.saldo)
                self.saldo = 0

            self.saldo_total = self._calc_saldo_total

            self._ext_saque(valor)

            print('Operação realizada com sucesso.')
        else:
            print('Falha ao realizar saque. Favor verificar valor e saldo.')

    def depositar(self: object, valor: float) -> None:
        """Dado valor > 0, acrescenta-o ao saldo da conta
        e atualiza o saldo total.

        Args:
            self (object): objeto (conta).
            valor (float): valor a ser acrescido à conta.
        """
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calc_saldo_total

            self._ext_deposito(valor)

            print('Operação realizada com sucesso.')
        else:
            print('Valor inválido.')

    def transferir(self: object, destino: object, valor: float) -> None:
        """Se 0 < valor <= saldo_total (conta de origem), de-
        cresce-o do saldo se valor <= saldo. Caso a última con-
        dição seja falsa, a diferença (valor - saldo) será de-
        crescida do limita e o saldo setado a 0.

        O valor é depositado na conta de destino e o saldo total
        de ambas as contas são atualizados.

        Args:
            self (object): objeto (conta de origem).
            destino (object): objeto (conta de destino)
            valor (float): valor a ser transferido.
        """
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.limite -= (valor - self.saldo)
                self.saldo = 0

            self.saldo_total = self._calc_saldo_total
            destino.saldo += valor
            destino.saldo_total = destino._calc_saldo_total

            self._ext_transferencia(destino.numero, valor)

            print('Operação realizada com sucesso.')
        else:
            print('Falha ao realizar transferência. Favor verificar valor e saldo.')

    def checar_saldo(self: object) -> None:
        print(f'Saldo total: {coin_float_to_str(self.saldo_total)}')

    def extrato(self: object) -> None:
        print('Extrato\n'
              '----------')

        for transacao in self._transacoes:
            print(transacao)
