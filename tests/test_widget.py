import pytest

from src.widget import get_date, mask_account_card


def test_get_date(iso_date: str) -> None:
    assert get_date(iso_date) == "11.03.2024"


def test_get_date_1(empty_str: str) -> None:
    with pytest.raises(ValueError):
        get_date(empty_str)


def test_mask_account_card_1(account_card_1: str) -> None:
    assert mask_account_card(account_card_1) == "Счет **4305"


def test_mask_account_card_2(account_card_2: str) -> None:
    assert mask_account_card(account_card_2) == "Visa Platinum 7000 79** **** 6361"
