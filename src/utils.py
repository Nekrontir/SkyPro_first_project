import json
import logging
import os

project_dir = os.path.dirname(os.getcwd())
log_file_path = os.path.join(project_dir, "logs", "utils_mod.log")  # путь для логов


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename=f"{log_file_path}",
    filemode="w",
)

utils_mod_logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла. Функция принимает-путь до JSON-файла(с именем файла),
    возвращает-список словарей с данными о транзакциях или пустой список
    """
    utils_mod_logger.info("Используется функция загрузки списка транзакций из JSON-файла")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            utils_mod_logger.info("Успешное получение списка транзакций")
            return data
        else:
            utils_mod_logger.warning("Список транзакций пуст")
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        utils_mod_logger.error("JSON-файла не существует или JSON-файл с ошибкой -> получение списка невозможно ")
        return []
