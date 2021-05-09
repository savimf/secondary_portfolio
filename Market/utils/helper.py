def coin_float_to_str(valor: float) -> str:
    """Recebe um float e o retorna formatado como
    string: R$ x,xxx.xx.

    Args:
        valor (float): valor a ser convertido, da
        forma xxxx.xx.

    Returns:
        str: valor convertido, da forma 'R$ x,xxx.xx.'
    """
    return f'R$ {valor:,.2f}'
