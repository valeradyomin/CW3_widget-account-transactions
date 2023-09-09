from utils.functions import get_transaction_objs, Transaction


class TestGetTransactionObjs:
    def test_get_transaction_objs(self):
        sample_data = [
            {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
             'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'},
            {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
             'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
             'to': 'Счет 18889008294666828266'},
            {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
             'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170',
             'to': 'Счет 96527012349577388612'}
        ]

        # Вызов функции чтобы получить объекты класса
        transactions = get_transaction_objs(sample_data)

        # Проверка что возвращаемое значение представляет собой список
        assert isinstance(transactions, list)

        # Проверка что каждый элемент в списке является экземпляром класса
        for transaction in transactions:
            assert isinstance(transaction, Transaction)

        # Проверка что функция возвращает правильное количество транзакций
        assert len(transactions) == len(sample_data)
