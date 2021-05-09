from datetime import date, datetime


def date_to_str(data: date) -> str:
    """Recebe um data em formato date e a retorna
    no formato 'dd/mm/aaaa'.

    Args:
        data (date): data a ser convertida.

    Returns:
        str: data no formato 'dd/mm/aaaa'.
    """
    return data.strftime('%d/%m/%Y')


def str_to_date(data: str) -> date:
    """Recebe um data no formato 'dd/mm/aaaa' e a
    retorna no formato date.

    Args:
        data (str): data a ser convertida.

    Returns:
        date: data no formato date.
    """
    return datetime.strptime(data, '%d/%m/%Y')


def coin_float_to_str(valor: float) -> str:
    """Recebe um float e o retorna formatado como
    string: R$ x,xxx.xx.
    Args:
        valor (float): valor a ser convertido, da
        forma xxxx.xx.
    Returns:
        str: valor convertido, da forma 'R$ x,xxx.xx.'
    """
    return f'RS {valor:,.2f}'
