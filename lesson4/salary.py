# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from number_utils import get_number_from_str
from sys import argv


def calc_salary(hours, rate, premium):
    return hours * rate + premium


help_text = """
salary, расчет заработной платы
    Использование: salary выработка_в_часах ставка_в_час [премия]
    Пример: salary 165 200 5300
            salary 165 200
"""

if len(argv) == 1 or argv[1].lower() == '?':
    print(help_text)
    exit()
elif len(argv) < 3:
    print('Не соответствует количество параметров')
    exit()

hours, rate, premium = [
    get_number_from_str(argv[1], min_value=0),
    get_number_from_str(argv[2], min_value=0),
    get_number_from_str(argv[3], min_value=0) if len(argv) > 3 else 0
]

params_is_valid = True
if hours is None:
    print('Неверное значение для параметра "выработка_в_часах"')
    params_is_valid = False

if rate is None:
    print('Неверное значение для параметра "ставка_в_час"')
    params_is_valid = False

if premium is None:
    print('Неверное значение для параметра "премия"')
    params_is_valid = False

if params_is_valid:
    salary = calc_salary(hours, rate, premium)
    print(f'Заработная плата: {salary}')
