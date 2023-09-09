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
