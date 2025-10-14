from datetime import datetime


def filter_by_state(dict_list: list, state_in_dict: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """

    new_dict_list: list = []
    if len(dict_list) == 0:
        return new_dict_list

    for dictionary in dict_list:
        if bool(dictionary) == 0:
            raise ValueError("В списке есть пустые словари")
    for dictionary in dict_list:
        if dictionary["state"] == state_in_dict:
            new_dict_list.append(dictionary)
    return new_dict_list


def sort_by_date(dict_list: list[dict], direction: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    """

    new_dict_list: list = []
    temp_dict_list: list = []
    for dict_in_list in dict_list:
        if bool(dict_in_list) == 0:
            continue
        else:
            temp_dict_list.append(dict_in_list)

    if len(temp_dict_list) == 0:
        return new_dict_list
    else:
        new_dict_list = sorted(temp_dict_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=direction)
        return new_dict_list
