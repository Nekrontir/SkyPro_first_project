from unittest.mock import Mock, patch

import pytest

from src.extraction_tools import get_transactions_from_excel_csv


@pytest.mark.parametrize(
    "file_name, expected_output, mock_data",
    [
        ("excel.xlsx", [{"id": 1, "amount": 100}], [{"id": 1, "amount": 100}]),
        ("excel.xls", [{"id": 2, "amount": 200}], [{"id": 2, "amount": 200}]),
        ("file.csv", [{"id": 3, "amount": 300}], [{"id": 3, "amount": 300}]),
        ("file.x", [], []),
    ],
)
def test_get_transactions_from_excel_csv_compact(file_name: str, expected_output: list, mock_data: list) -> None:

    mock_df = Mock()
    mock_df.to_dict.return_value = mock_data

    with (
        patch("src.extraction_tools.pd.read_excel") as mock_read_excel,
        patch("src.extraction_tools.pd.read_csv") as mock_read_csv,
    ):

        if file_name.endswith(("xlsx", "xls")):
            mock_read_excel.return_value = mock_df
        elif file_name.endswith("csv"):
            mock_read_csv.return_value = mock_df

        result = get_transactions_from_excel_csv(file_name)

        assert result == expected_output

        if file_name.endswith(("xlsx", "xls")):
            mock_read_excel.assert_called_once_with(file_name)
            mock_df.to_dict.assert_called_once_with(orient="records")
        elif file_name.endswith("csv"):
            mock_read_csv.assert_called_once_with(file_name, delimiter=";")
            mock_df.to_dict.assert_called_once_with(orient="records")


@pytest.mark.parametrize("file_name, error_type", [("error.xlsx", "Exception"), ("error.csv", "Exception")])
def test_get_transactions_from_excel_csv_errors(
    file_name: str, error_type: str, capsys: pytest.CaptureFixture
) -> None:

    if file_name.endswith(("xlsx", "xls")):
        with patch("src.extraction_tools.pd.read_excel", side_effect=Exception("File error")):
            result = get_transactions_from_excel_csv(file_name)

            assert result == []

            captured = capsys.readouterr()
            assert "При обработке файла возникла ошибка:" in captured.out

    elif file_name.endswith("csv"):
        with patch("src.extraction_tools.pd.read_csv", side_effect=Exception("File error")):
            result = get_transactions_from_excel_csv(file_name)

            assert result == []

            captured = capsys.readouterr()
            assert "При обработке файла возникла ошибка:" in captured.out
