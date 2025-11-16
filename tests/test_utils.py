import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions


@pytest.mark.parametrize(
    "file_content,expected_output",
    [
        (
            json.dumps(
                [
                    {
                        "id": 441945886,
                        "state": "EXECUTED",
                        "date": "2019-08-26T10:50:58.294041",
                        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Maestro 1596837868705199",
                        "to": "Счет 64686473678894779589",
                    }
                ]
            ),
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
        ("", []),
        ("{invalid json}", []),
    ],
)
def test_load_transactions(file_content: str, expected_output: list) -> None:

    with patch("builtins.open", mock_open(read_data=file_content)) as mock_file:
        result = load_transactions("dummy_path.json")

        assert result == expected_output
        mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")
