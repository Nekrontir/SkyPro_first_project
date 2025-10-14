import pytest

from src.widget import get_date, mask_account_card


def test_get_date(iso_date: str) -> None:
    assert get_date(iso_date) == "11.03.2024"


def test_get_date_1(empty_str: str) -> None:
    with pytest.raises(ValueError):
        get_date(empty_str)


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счёт 35383033474447895560", "Счёт **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108", "Счет **4108"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


def test_mask_card_number_raises_type_error(some_str: str) -> None:
    with pytest.raises(TypeError):
        mask_account_card(some_str)


def test_mask_card_number_raises_type_error_2(empty_str: str) -> None:
    with pytest.raises(TypeError):
        mask_account_card(empty_str)
