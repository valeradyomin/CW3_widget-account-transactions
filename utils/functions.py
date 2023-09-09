import json


def load_json(data_json):
    with open(data_json, "rt", encoding="utf-8") as file:
        transaction_data = json.load(file)
        return transaction_data

