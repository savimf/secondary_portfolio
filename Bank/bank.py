"""
BANCO

Aplicação onde, ao ser inicializada, exibirá ao usuário as opções: i) criar uma conta,
ii) realizar saque, iii) realizar depósito, iv) realizar transferência, v) listar contas,
ou vi) sair do sistema.
"""
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

# lista para armazenar as contas
contas: list = []


def main() -> None:
    """Função responsável pela execução do programa; chama a
    função menu()."""
    menu()


def menu() -> None:
    """Função responsável pela exibição e execução do menu.
    Após exibição, solicita ao usuário que insira uma das
    opções apresentadas e utiliza a entrada para chamar a
    função correspondente.
    """
    print('======================\n'
          '======== ATM =========\n'
          '====== Savi Bank =====\n'
          '======================\n')

    print('Selecione uma das opções abaixo: \n'
          '1 - Criar conta\n'
          '2 - Realizar saque\n'
          '3 - Realizar depósito\n'
          '4 - Realizar transferência\n'
          '5 - Listar contas\n'
          '6 - Extrato\n'
          '7 - Sair do sistema')

    opt: int = int(input())

    if opt in range(1, 7):
        opts[opt]()
    elif opt == 7:
        print('Volte sempre!')
        sleep(1)
        exit(0)
    else:
        print('Opção inválida.')
        sleep(1)
        menu()


def criar_conta() -> None:
    """Função que solicita ao usuário os dados necessários
    para a criação de uma conta (nome, CPF e data de nas-
    cimento). Ao final, a mesma é inserida à lista 'contas'.
    """
    print('Informe os dados do cliente.')

    cliente: Cliente = Cliente(input('Nome do cliente: '),
                               input('CPF do cliente: '),
                               input('Data de nascimento: '))

    contas.append(Conta(cliente))

    print('Conta criada com sucesso.')
    sleep(1)
    menu()


def saque() -> None:
    """Se len(contas) > 0, solicita ao usuário o número da
    conta e, caso presente em 'contas', solicitará o valor
    do saque, repassando-o ao método .sacar(), da classe
    Conta.
    """
    if len(contas) > 0:
        conta: Conta = buscar_conta_numero(
            int(input('Informe o número da sua conta: '))
        )

        if conta:
            conta.sacar(
                float(input('Informe o valor de saque: '))
            )
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    sleep(1)
    menu()


def deposito() -> None:
    """Se len(contas) > 0, solicita ao usuário o número da
    conta e, caso presente em 'contas', solicitará o valor
    do depósito, repassando-o ao método .depositar(), da
    classe Conta.
    """
    if len(contas) > 0:
        conta: Conta = buscar_conta_numero(
            int(input('Informe o número da conta: '))
        )

        if conta:
            conta.depositar(
                float(input('Informe o valor para depósito: '))
            )
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    sleep(1)
    menu()


def transferencia() -> None:
    """Se len(contas) > 0, solicita ao usuário o número
    da conta de origem e, caso presente em 'contas', so-
    licitará o número da conta de destino. Se ambas exis-
    tirem, o valor da transferência deve ser informado e
    todas as informações serão repassadas ao método
    .transferir(), da classe Conta.
    """
    if len(contas) > 0:
        c_origem: Conta = buscar_conta_numero(
            int(input('Informe o número da conta de destino: '))
        )

        if c_origem:
            c_destino: Conta = buscar_conta_numero(
                int(input('Informe o número da conta de destino: '))
            )

            if c_destino:
                c_origem.transferir(c_destino,
                                    float(input('Valor: ')))
            else:
                print('Conta de destino não encontrada.')
        else:
            print('Conta de origem não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    sleep(1)
    menu()


def listar_contas() -> None:
    """Se len(contas) > 0, exibirá ao usuário as
    contas listadas em 'contas'.
    """
    if len(contas) > 0:
        print('= Listagem de contas =')

        for conta in contas:
            print(f'{conta}\n'
                  '-------------------')
            sleep(.5)
    else:
        print('Ainda não há contas cadastradas.')
    sleep(1)
    menu()


def extrato() -> None:
    if len(contas) > 0:
        conta: Conta = buscar_conta_numero(
            int(input('Informe o número da conta: '))
        )

        if conta:
            conta.extrato()
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    sleep(1)
    menu()


def buscar_conta_numero(n: int) -> Conta:
    """Recebe um inteiro (número da conta) e, caso
    len(contas) > 0, retornará a conta corresponden-
    te ao número informado; caso contrário retornará
    None.

    Args:
        n (int): número da conta a ser procurada.

    Returns:
        Conta: conta associada ao número de entrada.
        Caso nenhuma seja encontrada, o retorno será
        None.
    """
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == n:
                c = conta
    return c


# dicionário para armazenar as funções
# que compõem o menu de opções
opts: dict = {1: criar_conta,
              2: saque,
              3: deposito,
              4: transferencia,
              5: listar_contas,
              6: extrato}

if __name__ == '__main__':
    main()
