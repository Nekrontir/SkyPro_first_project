from src.widget import get_date, mask_account_card

def test_get_date(iso_date):
    assert get_date(iso_date) == "11.03.2024"

def test_mask_account_card_1(account_card_1):
    assert mask_account_card(account_card_1) == "Счет **4305"

def test_mask_account_card_2(account_card_2):
    assert mask_account_card(account_card_2) == "Visa Platinum 7000 79** **** 6361"