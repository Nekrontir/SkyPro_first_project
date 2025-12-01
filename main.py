import os

from src.extraction_tools import get_transactions_from_excel_csv
from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

PATH_TO_FILE = os.path.dirname(__file__)

if __name__ == "__main__":
    print(
        """\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.
    Файл для обработки должен находится в директории data в корневом каталоге программы.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из XLS, XLSX-файла
    3. Получить информацию о транзакциях из CSV-файла
    """
    )
    user_choice: str = ""
    file_extension: str = ""
    while user_choice not in ["1", "2", "3"]:
        user_choice = input("Выбор пользователя: ")
        if user_choice == "1":
            file_extension = "JSON"
            break
        elif user_choice == "3":
            file_extension = "CSV"
            break
        elif user_choice == "2":
            file_extension = "excel"
            break
        else:
            print("\nВыбран несуществующий вариант, повторите выбор")

    print(f"\nДля обработки выбран {file_extension}-файл.")
    flag: bool = True
    file_name = ""
    while flag:
        file_name = input("\nВведите имя файла с расширением: ")
        if file_name.endswith((".json", ".xls", ".xlsx", ".csv")):
            flag = False
        else:
            print("Файл не введён или не содержит необходимое расширения")
    if file_extension == "JSON":
        data = load_transactions(os.path.join(PATH_TO_FILE, "data", file_name))
    else:
        data = get_transactions_from_excel_csv(os.path.join(PATH_TO_FILE, "data", file_name))

    print(
        """\nВведите статус, по которому необходимо выполнить фильтрацию, из доступных статусов: 
        EXECUTED, CANCELED, PENDING. Нажмите "Enter", что бы применить фильтр по умолчанию со статусом EXECUTED"""
    )

    user_filter = input("\nВведите статус для фильтрации: ").upper()
    if user_filter not in ["EXECUTED", "CANCELED", "PENDING"]:
        filter_data = filter_by_state(data)
        print('\nОперации отфильтрованы по статусу "EXECUTED"')
    else:
        filter_data = filter_by_state(data, user_filter)
        print(f'\nОперации отфильтрованы по статусу "{user_filter}"')

    sort_by_date_input = input("\nОтсортировать операции по дате? (Да/Нет): ")
    if sort_by_date_input.lower() in ["да", "yes"]:
        sort_by_date_dir = input("\nОтсортировать по возрастанию или по убыванию?: ")
        if sort_by_date_dir.lower() == "по возрастанию":
            sorted_data = sort_by_date(filter_data)
        elif sort_by_date_dir.lower() == "по убыванию":
            sorted_data = sort_by_date(filter_data, direction=True)
        else:
            sorted_data = sort_by_date(filter_data)
            print("\nНе корректный ввод направления сортировки, данные отсортированы по умолчанию: по убыванию")
    else:
        sorted_data = filter_data

    user_currency = input("\nВыводить только рублевые транзакции? (Да/Нет): ")
    if user_currency.lower() in ["да", "yes"]:
        filter_by_currency_data = list(filter_by_currency(sorted_data, "RUB"))
    else:
        filter_by_currency_data = sorted_data

    user_search = input("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ")
    if user_search.lower() in ["да", "yes"]:
        word_for_search = input("\nВведите слово для поиска: ")
        search_data = process_bank_search(filter_by_currency_data, word_for_search)
    else:
        search_data = filter_by_currency_data

    print(f"Всего банковских операций в выборке: {len(list(search_data))} ")
    if len(search_data) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transactions in search_data:
            date = get_date(transactions.get("date"))
            trans_info = transactions.get("description")
            print(f"\n{date} {trans_info}")
            trans_from = mask_account_card(transactions.get("from"))
            trans_to = mask_account_card(transactions.get("to"))
            print(f"{trans_from} -> {trans_to}")
            if user_choice == "1":
                amount = transactions.get("operationAmount", {}).get("amount")
                currency_code = transactions.get("operationAmount", {}).get("currency", {}).get("code")
                print(f"Сумма: {amount} {currency_code}\n")
            else:
                amount = transactions.get("amount")
                currency_code = transactions.get("currency_code")
                print(f"Сумма: {amount} {currency_code}\n")
