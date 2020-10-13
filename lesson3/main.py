from lesson3.prompt_utils import prompt_number


# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(x, y):
    return x / y


x = prompt_number(float, 'Введите делимое число')
if x is not None:
    y = prompt_number(float, 'Введите делитель')
    if y is not None:
        try:
            print(div(x, y))
        except ZeroDivisionError:
            print('Деление на 0')

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

print('\n' + '-' * 20 + '\n')


def print_user_data(first_name=None, last_name=None, birth_year=None, city=None, email=None, tel=None):
    default_text = 'нет данных'

    print(f'Имя: {first_name or default_text}')
    print(f'Фамилия: {last_name or default_text}')
    print(f'Год рождения: {birth_year or default_text}')
    print(f'Город проживания: {city or default_text}')
    print(f'Электронная почта: {email or default_text}')
    print(f'Номер телефона: {tel or default_text}')


# второй вариант
def print_user_data2(**kwargs):
    """
    print_user_data2(*[first_name, last_name, birth_year, city, email, tel])
    """

    default_text = 'нет данных'

    args = [
        ('Имя', kwargs.get('first_name') or default_text),
        ('Фамилия', kwargs.get('last_name') or default_text),
        ('Год рождения', kwargs.get('birth_year') or default_text),
        ('Город проживания', kwargs.get('city') or default_text),
        ('Электронная почта', kwargs.get('email') or default_text),
        ('Номер телефона', kwargs.get('tel') or default_text),
    ]

    for i in args:
        print(f'{i[0]}: {i[1]}')


first_name = input('Введите имя: ').strip()
last_name = input('Введите фамилию: ').strip()
birth_year = prompt_number(int, 'Введите год рождения')
city = input('Введите город проживания: ').strip()
email = input('Введите электронную почту: ').strip()
tel = input('Введите номер телефона: ').strip()

print()
print_user_data(
    first_name=first_name,
    last_name=last_name,
    birth_year=birth_year,
    city=city,
    email=email,
    tel=tel
)

# второй вариант
print()
print_user_data2(
    first_name=first_name,
    last_name=last_name,
    birth_year=birth_year,
    city=city,
    email=email,
    tel=tel
)

# второй вариант
print()
print_user_data2(**{
    'first_name': first_name,
    'last_name': last_name,
    'birth_year': birth_year,
    'city': city,
    'email': email,
    'tel': tel
})

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print('\n' + '-' * 20 + '\n')


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3], reverse=True)[:2])


print(my_func(23, 12, 34))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print('\n' + '-' * 20 + '\n')


def my_func(x, y):
    # первый способ
    # return 1 / (x ** -y) if y < 0 else x ** y

    # второй способ (цикл)
    if y == 0:
        return 1

    res = x
    for i in range(1, abs(y)):
        res *= x

    return res if y > 0 else 1/res


x = prompt_number(float, 'Введите положительное число', min_value=0)
if x is not None:
    y = prompt_number(int, 'Введите целое отрицательное число', max_value=-1)
    if y is not None:
        z = my_func(x, y)

        print(f'{x} в степени {y}: {z}')

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

print('\n' + '-' * 20 + '\n')


def to_float_or_zero(x):
    try:
        return float(x)
    except ValueError:
        return 0.0


total = 0
stop = False

print('Введите числа разделенные пробелом (для завершения введите "!" вместо числа)')
while not stop:
    nums = input('>: ')
    nums = nums.split()

    for i, v in enumerate(nums):
        if v == '!':
            stop = True
            break
        else:
            total += to_float_or_zero(nums[i])

    print(f'Итого: {total}')

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

print('\n' + '-' * 20 + '\n')


def int_func(word: str):
    return word.capitalize()


text = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(' '.join(map(int_func, text.split())))
