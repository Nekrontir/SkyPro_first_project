import pytest
from pytest import CaptureFixture

from src.decorators import log_to_file_or_console


def test_log_to_file_or_console(capsys: CaptureFixture[str]) -> None:
    @log_to_file_or_console(None)
    def func() -> int:
        return 0

    assert func() == 0
    captured = capsys.readouterr()
    assert captured.out == f"{func.__name__} ok!\n"



def test_log_to_file_or_console_error(capsys: CaptureFixture[str]) -> None:
    @log_to_file_or_console(None)
    def func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        func()

    captured = capsys.readouterr()
    assert "func error: Test error. Inputs: (), {}.\n" in captured.out
