import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты для filter_by_currency
def test_filter_by_currency_usd_returns_2_transactions(transactions: list) -> None:
    """Тест фильтрации по USD"""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_rub_returns_1_transaction(transactions: list) -> None:
    """Тест фильтрации по RUB"""
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_filter_by_currency_eur_returns_empty(transactions: list) -> None:
    """Тест фильтрации по несуществующей валюте"""
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_lazy_loading(transactions: list) -> None:
    """Тест ленивой загрузки"""
    generator = filter_by_currency(transactions, "USD")

    first = next(generator)
    assert first["id"] == 939719570

    second = next(generator)
    assert second["id"] == 142264268

    with pytest.raises(StopIteration):
        next(generator)


# Тесты для transaction_descriptions
def test_transaction_descriptions_returns_all(transactions: list) -> None:
    """Тест получения всех описаний"""
    result = list(transaction_descriptions(transactions))
    expected = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]
    assert result == expected


def test_transaction_descriptions_lazy_loading(transactions: list) -> None:
    """Тест ленивой загрузки описаний"""
    generator = transaction_descriptions(transactions)

    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"

    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_empty_list(empty_list: list) -> None:
    """Тест с пустым списком"""
    result = list(transaction_descriptions(empty_list))
    assert result == []


# Тесты для card_number_generator
def test_card_number_generator_small_range() -> None:
    """Тест маленького диапазона"""
    result = list(card_number_generator(1, 3))
    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert result == expected


def test_card_number_generator_single_number() -> None:
    """Тест одного числа"""
    result = list(card_number_generator(42, 42))
    assert result == ["0000 0000 0000 0042"]


def test_card_number_generator_large_numbers() -> None:
    """Тест больших чисел"""
    result = list(card_number_generator(9999999999999998, 9999999999999999))
    expected = ["9999 9999 9999 9998", "9999 9999 9999 9999"]
    assert result == expected


def test_card_number_generator_lazy_loading() -> None:
    """Тест ленивой генерации"""
    generator = card_number_generator(1, 3)

    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration):
        next(generator)


# Тесты на ошибки для card_number_generator
def test_card_number_generator_invalid_start() -> None:
    """Тест ошибки при начале < 1"""
    with pytest.raises(ValueError, match="Диапазон должен быть от 1 до 9999999999999999"):
        list(card_number_generator(0, 5))


def test_card_number_generator_invalid_end() -> None:
    """Тест ошибки при конце > максимума"""
    with pytest.raises(ValueError, match="Диапазон должен быть от 1 до 9999999999999999"):
        list(card_number_generator(1, 10000000000000000))


def test_card_number_generator_invalid_range() -> None:
    """Тест ошибки когда начало > конца"""
    with pytest.raises(ValueError, match="Начальное значение не может быть больше конечного"):
        list(card_number_generator(10, 5))
