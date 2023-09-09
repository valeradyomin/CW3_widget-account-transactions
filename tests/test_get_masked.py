from utils.functions import get_masked


def test_get_masked():
    # проверка преобразования текстовой информации для финального вывода
    assert get_masked(None) == "Открытие вклада"
    assert get_masked("Счет 01234567890123456789") == "Счет **6789"
    assert get_masked("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert get_masked("Visa Classic 2842878893689012") == "Visa Classic 2842 87** **** 9012"
