"""
GAME

Descrição:
Aplicação que, ao ser inicializada, solicitará ao usuário um nível de
dificuldade e, após isso, apresentará, aleatoriamente, uma expressão a
ser resolvida e o resultado verificado.

As operações serão limitadas em soma, subtração e multiplicação. Se o usu-
ário acertar a resposta, seu score aumentará em 1. Conforme o nível de di-
ficuldade aumenta, o intervalo dos números gerados também aumenta.
"""
from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade = int(input('Informe o nível de dificuldade '\
    'desejado (1, 2, 3 ou 4): '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado da operação abaixo.')
    calc.show_op()

    res = int(input('Resposta: '))

    if calc.check_resposta(res):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar = int(input('Desejar continuar? (1 - sim, 0 - não): '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')

if __name__ == '__main__':
    main()
