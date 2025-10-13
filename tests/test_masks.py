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


@pytest.mark.parametrize(
    "number, expected", [(7000792289606361, "7000 79** **** 6361"), (7034767284676798, "7034 76** **** 6798")]
)
def test_mask_card_number_1(number: int, expected: str) -> None:
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "acc_number, expected",
    [(73654108430135874305, "**4305"), (7365410843013587430523423, "**3423"), (73654108, "**4108")],
)
def test_mask_account_1(acc_number: int, expected: str) -> None:
    assert get_mask_account(acc_number) == expected
