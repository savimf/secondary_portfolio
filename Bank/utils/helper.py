from datetime import date, datetime


def date_to_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_to_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def coin_float_to_str(valor: float) -> str:
    return f'RS {valor:,.2f}'
