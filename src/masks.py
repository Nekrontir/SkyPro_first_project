def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по шаблону XXXX XX** **** XXXX
    """

    card_str = str(card_number)

    masked_card_number = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """

    account_str = str(account_number)

    masked_account_number = "**" + account_str[-4:]
    return masked_account_number
