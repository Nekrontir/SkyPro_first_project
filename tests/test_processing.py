import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state(dict_list: list) -> None:
    assert filter_by_state(dict_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2(empty_dict_list: list) -> None:
    with pytest.raises(ValueError):
        filter_by_state(empty_dict_list)


@pytest.mark.parametrize(
    "dict_lists, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ([], "CANCELED", []),
        ([], "EXECUTED", []),
    ],
)
def test_filter_by_state_3(dict_lists: list, state: str, expected: list) -> None:
    assert filter_by_state(dict_lists, state) == expected


def test_sort_by_date(dict_list: list) -> None:
    assert sort_by_date(dict_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(empty_dict_list: list) -> None:
    assert sort_by_date(empty_dict_list) == []


def test_sort_by_date_3(half_empty_dict_list: list) -> None:
    assert sort_by_date(half_empty_dict_list) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]


def test_process_bank_search(transactions_2: list) -> None:
    assert process_bank_search(transactions_2, "Перевод") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
    ]


def test_process_bank_operations(transactions_2: list) -> None:
    assert process_bank_operations(transactions_2, []) == {}


def test_process_bank_operations2(transactions_2: list) -> None:
    assert process_bank_operations(transactions_2, ["Перевод организации"]) == {"Перевод организации": 1}
