

# функция преобразует строку {string} в число типа {num_type} в пределах {min_value} и {max_value}
# Если преобразование невозможно (с учетом пределов) возвращает None, иначе число
def get_number_from_str(string, num_type=float, min_value=None, max_value=None):
    try:
        num = num_type(string)
    except ValueError:
        return None

    if (min_value is not None and num < min_value) or (max_value is not None and num > max_value):
        return None

    return num


# функция проверяет строку {string} на соответствие числу типа {num_type} в пределах {min_value} и {max_value}
def str_is_correct_number(string, num_type=float, min_value=None, max_value=None):
    return get_number_from_str(string, num_type, min_value, max_value) is not None
