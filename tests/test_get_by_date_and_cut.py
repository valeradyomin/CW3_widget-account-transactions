import pytest

from utils.functions import get_by_date_and_cut, Transaction


def test_get_by_date_and_cut():
    executed_lst = [
        Transaction(id=1, state="", date="2023-09-09", amount=100, currency="",
                    description="", from_account="", to_account=""),
        Transaction(id=2, state="", date="2023-09-08", amount=200, currency="",
                    description="", from_account="", to_account=""),
        Transaction(id=3, state="", date="2023-09-07", amount=300, currency="",
                    description="", from_account="", to_account="")
    ]
    items_cut = 2

    selected_operations_lst = get_by_date_and_cut(executed_lst, items_cut)

    assert len(selected_operations_lst) == items_cut
    assert selected_operations_lst[0].id == 1
    assert selected_operations_lst[1].id == 2
    with pytest.raises(IndexError):
        assert selected_operations_lst[2].date == "2023-09-07"

