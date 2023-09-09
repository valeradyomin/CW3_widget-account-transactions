import os
from datetime import date

from utils.functions import load_json, get_transaction_objs, get_executed_operations, get_by_date_and_cut, get_masked


def main():
    data = load_json(os.path.join("./data/operations.json"))
    transactions_objs_lst = get_transaction_objs(data)
    executed_operations_objs_lst = get_executed_operations(transactions_objs_lst, target_state="EXECUTED")
    selected_operations_objs_lst = get_by_date_and_cut(executed_operations_objs_lst, 5)
    for operation in selected_operations_objs_lst:
        print()
        print(f""
              f"{date.fromisoformat(operation.date[0:10]).day}."
              f"{date.fromisoformat(operation.date[0:10]).month}."
              f"{date.fromisoformat(operation.date[0:10]).year} {operation.description}")
        print(f"{get_masked(operation.from_account)} -> {get_masked(operation.to_account)}")
        print(f"{operation.amount} {operation.currency}")


if __name__ == "__main__":
    main()
