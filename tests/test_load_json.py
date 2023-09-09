import json

from utils.functions import load_json


def test_load_json():
    # Создание временного файла JSON с тестовыми данными
    data = {
        "transactions": [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
            {"id": 3, "amount": 300}
        ]
    }
    with open("test_data.json", "w") as file:
        json.dump(data, file)

    # Вызов функции load_json с временным файлом
    result = load_json("test_data.json")

    # Проверка, что возвращаемое значение соответствует ожидаемым результатам
    assert "transactions" in result
    assert len(result["transactions"]) == 3
    assert result["transactions"][0]["id"] == 1
    assert result["transactions"][0]["amount"] == 100


def test_load_json_returns_list():
    # Создание временного файла JSON с тестовыми данными
    data = [1, 2, 3]
    with open("test_data.json", "w") as file:
        json.dump(data, file)

    # Вызов функции load_json с временным файлом
    result = load_json("test_data.json")

    # Проверка, что возвращаемое значение является списком
    assert isinstance(result, list)