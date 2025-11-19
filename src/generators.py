from collections.abc import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по коду валюты и возвращает итератор
    """

    for transaction in transactions:
        try:
            code = transaction["operationAmount"]["currency"]["code"]
            if code == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX
    """

    if start < 1 or end > 9999999999999999:
        raise ValueError("Диапазон должен быть от 1 до 9999999999999999")

    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    current = start

    while current <= end:
        card_str = str(current).zfill(16)
        formatted_card = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"

        yield formatted_card
        current += 1
