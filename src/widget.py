from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """
    Принимает строку содержащую тип и номер карты или счета, возвращает строку с замаскированным номером или счётом
    """
    if "счет" in account_card.lower() or "счёт" in account_card.lower():
        account_number = get_mask_account(int(account_card[account_card.index(" ") + 1 :]))
        mask_account = account_card.replace(account_card[account_card.index(" ") + 1 :], account_number)
        return mask_account
    else:
        index = 0
        for digit in account_card:
            if digit.isdigit():
                index = account_card.index(digit)
                break
        card_number = get_mask_card_number(int(account_card[index:]))
        mask_card = account_card.replace(account_card[index:], card_number)
        return mask_card
