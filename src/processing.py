def filter_by_state(dict_list: list[dict], state_in_dict: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """

    new_dict_list = []

    for dictionary in dict_list:
        if dictionary["state"] == state_in_dict:
            new_dict_list.append(dictionary)

    return new_dict_list


def sort_by_date(dict_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    """
    pass
