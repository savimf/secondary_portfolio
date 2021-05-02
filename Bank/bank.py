"""
BANCO

Aplicação onde, ao ser inicializada, exibirá ao usuário as opções: i) criar uma conta,
ii) realizar saque, iii) realizar depósito, iv) realizar transferência, v) listar contas,
ou vi) sair do sistema.
"""
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: list = []

def main() -> None:
    menu()


def menu() -> None:
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
          '6 - Sair do sistema')

    opt: int = int(input())

    if opt in range(1, 6):
        opts[opt]()
    elif opt == 6:
        print('Volte sempre!')
        sleep(1)
        exit(0)
    else:
        print('Opção inválida.')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente.')

    cliente: Cliente = Cliente(input('Nome do cliente: '),
                               input('CPF do cliente: '),
                               input('Data de nascimento: '))

    contas.append(Conta(cliente))

    print('Conta criada com sucesso.')
    sleep(1)
    menu()


def saque() -> None:
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


def buscar_conta_numero(n: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == n:
                c = conta
    return c


opts: dict = {1: criar_conta,
              2: saque,
              3: deposito,
              4: transferencia,
              5: listar_contas}

if __name__ == '__main__':
    main()
