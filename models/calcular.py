from random import randint

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:  # somente posicional
        self.dificuldade: int = dificuldade
        self.valor1: int = self._gerar_valor
        self.valor2: int = self._gerar_valor
        self.operacao: int = randint(1, 3)  # 1: +, 2: -, 3: x
        self.resultado: int = self._gerar_resultado

    def __str__(self: object) -> str:
        op: str = ''

        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'

        return f'Valor 1: {self.valor1} \n'\
               f'Valor2: {self.valor2} \n'\
               f'Dificuldade: {self.dificuldade} \n'\
               f'Operação: {op}'


    def __conv_op(a: int, b: int, op: int) -> int:
        """Recebe dois parâmetros e o índice da operação
        a ser executada e retorna o resultado.

        Args:
            a (int): 1o valor de entrada
            b (int): 2o valor de entrada
            op (int): índice da operação (1: +, 2: -, 3: *)

        Returns:
            int: a {op} b
        """
        if op == 1:
            return a + b
        elif op == 2:
            return a - b
        return a * b


    def __dif_random(dif: int) -> int:
        """Recebe um inteiro de 1 até 4 e retorna um
        número aleatório pertencente a um dado inter-
        valo.

        Args:
            dif (int): inteiro (1, 2, 3, 4)

        Returns:
            int: 1: n.aleat (0, 10)
                 2: n.aleat (0, 100)
                 3: n.aleat (0, 1000)
                 4: n.aleat (0, 10000)
        """
        dif_dict: dict = {1: randint(0, 10),
                          2: randint(0, 100),
                          3: randint(0, 1000),
                          4: randint(0, 10_000)}
        return dif_dict.get(dif)


    @property
    def _gerar_valor(self: object) -> int:
        """Retorna um número aleatório baseado na
        dificuldade de entrada.

        Args:
            self (object): objeto

        Returns:
            int: número aleatório
        """
        if self.dificuldade in range(1, 4):
            return Calcular.__dif_random(self.dificuldade)
        return randint(0, 100_000)


    @property
    def _gerar_resultado(self: object) -> int:
        """Retorna o resultado da operação de acordo com
        os atributos instanciados do objeto.

        Args:
            self (object): objeto

        Returns:
            int: valor1 {op} valor2
        """
        return Calcular.__conv_op(self.valor1,
                                  self.valor2,
                                  self.operacao)

    @property
    def _op_simbolo(self: object) -> str:
        """Retorna o símbolo que representa a ope-
        ração matemática associada ao atributo ope-
        ração.

        Args:
            self (object): objeto

        Returns:
            str: +, - ou *
        """
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        return '*'


    def check_resposta(self: object, resposta: int) -> bool:
        """Confere se a resposta de entrada, fornecida pelo
        usuário é igual ao resultado da operação.

        Args:
            self (object): objeto
            resposta (int): resposta do usuário

        Returns:
            bool: True se a resposta for correta,
                  False caso contrário.
        """
        check: bool = False

        if self.resultado == resposta:
            print('Resposta correta.')
            check = True
        else:
            print('Resposta errada.')
            print(f'{self.valor1} {self._op_simbolo} {self.valor2} = '\
                  f'{self.resultado}')
        return check


    def show_op(self: object) -> None:
        """Imprime na tela a expressão matemática a ser
        resolvida pelo usuário, de acordo com os atribu-
        tos do objeto.

        Args:
            self (object): objeto
        """
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
