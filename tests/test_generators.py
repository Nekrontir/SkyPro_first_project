import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты для filter_by_currency
def test_filter_by_currency_usd_returns_2_transactions(transactions: list) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3


def test_filter_by_currency_rub_returns_1_transaction(transactions: list) -> None:
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 2
    assert result[0]["id"] == 873106923


def test_filter_by_currency_eur_returns_empty(transactions: list) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


# Тесты для transaction_descriptions
def test_transaction_descriptions_returns_all(transactions: list) -> None:
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_lazy_loading(transactions: list) -> None:
    generator = transaction_descriptions(transactions)

    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_empty_list(empty_list: list) -> None:
    result = list(transaction_descriptions(empty_list))
    assert result == []


# Тесты для card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (42, 42, ["0000 0000 0000 0042"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_different_range(start: int, stop: int, expected: list) -> None:
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_lazy_loading() -> None:
    generator = card_number_generator(1, 3)

    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration):
        next(generator)


# Тесты на ошибки для card_number_generator
def test_card_number_generator_invalid_start() -> None:
    with pytest.raises(ValueError, match="Диапазон должен быть от 1 до 9999999999999999"):
        list(card_number_generator(0, 5))


def test_card_number_generator_invalid_end() -> None:
    with pytest.raises(ValueError, match="Диапазон должен быть от 1 до 9999999999999999"):
        list(card_number_generator(1, 10000000000000000))


def test_card_number_generator_invalid_range() -> None:
    with pytest.raises(ValueError, match="Начальное значение не может быть больше конечного"):
        list(card_number_generator(10, 5))
