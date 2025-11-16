from unittest.mock import Mock, patch

from src.external_api import get_amount_from_transaction


def test_get_amount_from_transaction(transaction_rub: dict) -> None:
    result = get_amount_from_transaction(transaction_rub)
    assert result == 31957.58


def test_usd_transaction_converts_via_api(transaction_usd: dict) -> None:
    with (
        patch("src.external_api.load_dotenv") as mock_load_dotenv,
        patch("src.external_api.os.getenv") as mock_getenv,
        patch("src.external_api.requests.request") as mock_request,
    ):
        mock_getenv.return_value = "fake_api_key"
        mock_response = Mock()
        mock_response.json.return_value = {"result": 750000.0}
        mock_request.return_value = mock_response

        result = get_amount_from_transaction(transaction_usd)
        assert result == 750000.0

        mock_load_dotenv.assert_called_once()
        mock_getenv.assert_called_with("API_KEY")
        mock_request.assert_called_once()
