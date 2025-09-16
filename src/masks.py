def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по шаблону XXXX XX** **** XXXX
    """

    card_str = str(card_number)

    if len(card_str) != 16:
        return "Номер карты должен содержать 16 цифр"
    elif not card_str.isdigit():
        return "Номер карты должен состоять из цифр"
    else:
        masked_card_number = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
        return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """

    account_str = str(account_number)

    if len(account_str) <= 6:
        return "Номер счёта должен содержать минимум из 6 цифр"
    elif not account_str.isdigit():
        return "Номер счёта должен состоять из цифр"
    else:
        masked_account_number = "**" + account_str[-4:]
        return masked_account_number
