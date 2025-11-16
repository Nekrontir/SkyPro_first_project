import os

import requests
from dotenv import load_dotenv


def get_amount_from_transaction(transaction: dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    если валюта транзакции иная - то при помощи Exchange Rates Data API производится конвертация
    суммы в рубли.
    """
    valid_currency_code = "RUB"

    if transaction.get("operationAmount", {}).get("currency", {}).get("code") == valid_currency_code:
        amount = float(transaction.get("operationAmount", {}).get("amount"))
        return amount
    else:
        currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        amount = transaction.get("operationAmount", {}).get("amount")
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={valid_currency_code}\
        &from={currency_code}&amount={amount}"
        payload = {None: any}
        headers = {"apikey": api_key}

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        amount = float(result.get("result"))
        return amount
