from utils.functions import get_executed_operations, Transaction


def test_get_executed_operations_single_executed_transaction():
    target_state = "EXECUTED"
    transactions = [
        Transaction(id=1, state=target_state, date="", amount="", currency="",
                    description="", from_account="", to_account="")
    ]
    result = transactions
    assert get_executed_operations(transactions, target_state) == result


def test_get_executed_operations_multiple_transactions():
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
