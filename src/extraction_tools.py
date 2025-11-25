import pandas as pd


def get_transactions_from_excel_csv(path_to_file: str) -> list[dict]:
    """
    Функция для извлечения списка транзакций из xls,xlsx,csv - файлов.
    На вход принимает полный путь расположения файла с указанием расширения,
    на выходе функции список словарей.
    """
    if path_to_file.endswith(("xlsx", "xls")):
        try:
            df = pd.read_excel(path_to_file)
            dict_list = df.to_dict(orient="records")
            return dict_list
        except Exception as error:
            print(f"При обработке файла возникла ошибка: {error}")
            return []
    elif path_to_file.endswith("csv"):
        try:
            df = pd.read_csv(path_to_file, delimiter=";")
            dict_list = df.to_dict(orient="records")
            return dict_list
        except Exception as error:
            print(f"При обработке файла возникла ошибка: {error}")
            return []
    else:
        return []

