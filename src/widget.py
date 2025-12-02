from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Принимает строку содержащую тип и номер карты или счета, возвращает строку с замаскированным номером или счётом
    """
    try:
        if "счет" in account_card.lower() or "счёт" in account_card.lower():
            number_index = 0
            for digit in account_card:
                if digit.isdigit():
                    number_index = account_card.index(digit)
                    break
            account_number = get_mask_account(int(account_card[number_index:]))
            mask_account = account_card.replace(account_card[number_index:], account_number)
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
    except (ValueError, AttributeError):
        return ""


def get_date(date_time: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    if len(date_time) == 0:
        raise ValueError("В строке нет символов")

    iso_date = datetime.fromisoformat(date_time)
    year_month_day = str(iso_date)[:10]
    split_date = year_month_day.split("-")
    date = f"{split_date[2]}.{split_date[1]}.{split_date[0]}"
    return date
