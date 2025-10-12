import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_number: int) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_mask_card_number_raises_value_error(empty_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(empty_number)


def test_mask_account(account_number: int) -> None:
    assert get_mask_account(account_number) == "**4305"


def test_mask_account_raises_value_error(empty_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account(empty_number)
