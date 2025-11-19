import logging
import os

project_dir = os.path.dirname(os.getcwd())
log_file_path = os.path.join(project_dir, "logs", "masks_mod.log")  # путь для логов


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename=f"{log_file_path}",
    filemode="w",
)

masks_mod_logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты из 16 цифр по шаблону XXXX XX** **** XXXX
    """
    masks_mod_logger.info(f"Использование функции маскировки номера карты - {card_number}")
    card_str = str(card_number)

    if len(card_str) < 16 or len(card_str) > 16:
        masks_mod_logger.error("Вызвано исключение -> В номере карты не 16 цифр")
        raise ValueError("Неверное количество цифр в номере карты")

    else:
        masked_card_number = card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:]
        masks_mod_logger.info("Успешное выполнение функции маскировки")
        return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по шаблону **XXXX
    """
    masks_mod_logger.info(f"Использование функции маскировки номера счёта - {account_number}")
    account_str = str(account_number)

    if len(account_str) < 5:
        masks_mod_logger.error("Вызвано исключение -> В номере счёта меньше 5 цифр")
        raise ValueError("Слишком короткий номер счёта")
    else:
        masked_account_number = "**" + account_str[-4:]
        masks_mod_logger.info("Успешное выполнение функции маскировки")
        return masked_account_number
