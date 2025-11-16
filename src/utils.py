import json


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла. Функция принимает-путь до JSON-файла(с именем файла),
    возвращает-список словарей с данными о транзакциях или пустой список
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
