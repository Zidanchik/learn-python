from number_utils import get_number_from_str


# функция запрашивает у пользователя число типа {num_type}
# и возвращает его или None в случае отмены ввода.
# Значение отмены ввода передается через {cancel_value}.
# Запрос будет повторяться пока пользователь не введет корректное число или не отменит ввод
# Текст запрос передается через {text}, либо используется текст по умолчанию.
# Текст некорректного значения передается через {err_text}, либо используется текст по умолчанию.
# Минимальное и максимальное значения передеются через {min_value} и {max_value} соответственно
def prompt_number(num_type=float, text=None, err_text=None, cancel_value='', min_value=None, max_value=None):
    if text is None:
        text = 'Введите число'

    if err_text is None:
        err_text = 'Введенное значение не является допустимым'

    while True:
        num = input(f'{text} (для отмены введите "{cancel_value}"): ')
        if num == cancel_value:
            return None

        num = get_number_from_str(num, num_type, min_value, max_value)
        if num is not None:
            return num

        print(err_text)
