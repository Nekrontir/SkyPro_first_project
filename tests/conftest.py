import pytest


@pytest.fixture
def card_number():
    return 7000792289606361


@pytest.fixture
def account_number():
    return 73654108430135874305

@pytest.fixture
def iso_date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def account_card_1():
    return "Счет 73654108430135874305"

@pytest.fixture
def account_card_2():
    return "Visa Platinum 7000792289606361"


