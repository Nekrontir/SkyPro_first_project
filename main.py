
from src.extraction_tools import get_transactions_from_excel_csv
from src.processing import filter_by_state
from src.utils import load_transactions
import os


PATH_TO_FILE = os.path.dirname(__file__)

if __name__ == "__main__":
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Файл для обработки должен находится в директории data в корневом каталоге программы.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV, XLS, XLSX-файла
""")
    user_choice : str = ""
    file_extension : str = ""
    while user_choice not in  ['1', '2', '3']:
        user_choice = input("Выбор пользователя: ")
        if user_choice == '1':
            file_extension = "JSON"
            break
        elif user_choice == '2':
            file_extension = "CSV"
            break
        elif user_choice == '3':
            file_extension = "excel"
            break
        else:
            print("Выбран несуществующий вариант, повторите выбор")
    print(f"Для обработки выбран {file_extension}-файл.")
    file_name = input("Введите имя файла с расширением: ")
    if file_extension == 'JSON':
        data = load_transactions(os.path.join(PATH_TO_FILE, "data", file_name))
    else:
        data = get_transactions_from_excel_csv(os.path.join(PATH_TO_FILE, "data", file_name))

    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
Нажмите "Enter", что бы применить фильтр по умолчанию со статусом EXECUTED""")

    user_filter = input("Введите статус для фильтрации: ").upper()
    if user_filter not in ['EXECUTED', 'CANCELED', 'PENDING']:
        filter_data = filter_by_state(data)
    else:
        filter_data = filter_by_state(data, user_filter)

    print(filter_data)