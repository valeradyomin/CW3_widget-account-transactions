import json

from utils.my_class import Transaction


def load_json(data_json):
    with open(data_json, "rt", encoding="utf-8") as file:
        transaction_data = json.load(file)
        return transaction_data


def get_transaction_objs(data: list):
    transactions = []
    for item in data:
        operation_amount = item.get("operationAmount", {})
        amount = operation_amount.get("amount", None)
        currency = operation_amount.get("currency", {}).get("name", None)

        transaction = Transaction(
            id=item.get("id", None),
            state=item.get("state", None),
            date=item.get("date", None),
            amount=amount,
            currency=currency,
            description=item.get("description", None),
            from_account=item.get("from", None),
            to_account=item.get("to", None)
        )
        transactions.append(transaction)
    return transactions


def get_executed_operations(transactions: list, target_state: str):
    executed_lst = []
    for transaction in transactions:
        if target_state == transaction.state:
            executed_lst.append(transaction)
    return executed_lst


def get_by_date_and_cut(executed_lst: list, items_cut: int):
    executed_lst_sorted = sorted(executed_lst, key=lambda x: x.date, reverse=True)
    selected_operations_lst = executed_lst_sorted[0:items_cut]
    return selected_operations_lst


def get_masked(item):
    if item is None:
        return "Открытие вклада"

    if "Счет" in item:
        tail = item[len(item.rstrip('0123456789')):]
        new_tail = f"{(len(tail) - 18) * '*'}{tail[-4:]}"
    else:
        tail = item[len(item.rstrip('0123456789')):]
        new_tail = f"{tail[0:4]} {tail[4:6]}** **** {tail[12:16]}"

    return f"{item.rstrip('0123456789')}{new_tail}"
