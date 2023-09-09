from utils.functions import get_executed_operations, Transaction


def test_get_executed_operations_single_executed_transaction():
    # проверка функции когда есть только одна транзакция и ее состояние соответствует target_state.
    target_state = "EXECUTED"
    transactions = [
        Transaction(id=1, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account="")
    ]
    result = transactions
    assert get_executed_operations(transactions, target_state) == result


def test_get_executed_operations_multiple_transactions():
    # проверка функции когда в списке несколько транзакций одни из которых имеют состояние target_state, а другие - нет.
    target_state = "EXECUTED"
    transactions = [
        Transaction(id=1, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account=""),
        Transaction(id=2, state="PENDING", date="", amount="", currency="",
                    description="", from_account="", to_account=""),
        Transaction(id=3, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account="")
    ]
    result = [
        Transaction(id=1, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account=""),
        Transaction(id=3, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account="")
    ]
    assert get_executed_operations(transactions, target_state) != result
