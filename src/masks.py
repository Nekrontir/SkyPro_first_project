def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты из 16 цифр по шаблону XXXX XX** **** XXXX
    """

    card_str = str(card_number)

    if len(card_str) < 16 or len(card_str) > 16:
        raise ValueError("Неверное количество цифр в номере карты")
    else:
        masked_card_number = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
        return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """

    account_str = str(account_number)

    if len(account_str) < 5:
        raise ValueError("Слишком короткий номер счёта")
    else:
        masked_account_number = "**" + account_str[-4:]
        return masked_account_number
