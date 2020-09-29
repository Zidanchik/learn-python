import time


def isnumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# функция запрашивает у пользователя число типа {num_type}
# и возвращает его или None в случае отмены ввода.
# Значение отмены ввода передается через {cancel_value}.
# Запрос будет повторяться пока пользователь не введет корректное число или не отменит ввод
# Текст запрос передается через {text}, либо используется текст по умолчанию.
# Текст некорректного значения передается через {err_text}, либо используется текст по умолчанию.
# Возможность ввода отрицательных чисел указывается через {allow_neg}
def prompt_number(num_type=float, text=None, err_text=None, allow_neg=True, cancel_value = ''):
    if text is None:
        text = 'Введите число'

    if err_text is None:
        err_text = 'Введенное значение не является числом'

    while True:
        num = input(f'{text} (для отмены введите "{cancel_value}"): ')

        if num == cancel_value:
            return None

        try:
            num = num_type(num)
        except ValueError:
            print(err_text)
            continue

        if not allow_neg and num < 0:
            print(err_text)
        else:
            return num


# функция запрашивает у пользователя положительное число
def prompt_pos_number(text):
    return prompt_number(float, text, 'Введенное значение не является положительным числом', False)


# функция запрашивает у пользователя целое положительное число
def prompt_pos_int_number(text):
    return prompt_number(int, text, 'Введенное значение не является целым положительным числом', False)


# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

x = input('Введите строку: ')
print(f'Вы ввели: {x}')

x = prompt_number()
if x is not None:
    print(f'Вы ввели: {x}')

# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('\n' + '-' * 20 + '\n')

x = prompt_pos_int_number('Введите время в секундах')
if x is not None:
    x = time.gmtime(int(x))
    print(f'{x.tm_hour:02}:{x.tm_min:02}:{x.tm_sec:02}')

# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 2.
# Считаем 2 + 22 + 222 = 246.

print('\n' + '-' * 20 + '\n')

x = prompt_pos_int_number('Введите целое положительное число n')
if x is not None:
    x = str(x)
    print(f'Сумма n + nn + nnn: {int(x) + int(x * 2) + int(x * 3)}')

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('\n' + '-' * 20 + '\n')

x = prompt_pos_int_number('Введите целое положительное число')
if x is not None:
    x = int(x)
    max_digit = 0

    while x > 0:
        x, digit = divmod(x, 10)
        max_digit = max(max_digit, digit)

    print(f'Наибольшая цифра: {max_digit}')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('\n' + '-' * 20 + '\n')

debet = prompt_pos_number('Введите размер выручки (положительное число)')
credit = prompt_pos_number('Введите размер издержек (положительное число)')

if debet is not None and credit is not None:
    balance = debet - credit

    if balance == 0:
        print('Без прибыли и убытков')
    elif balance > 0:
        print(f'Прибыль: {balance:.2f}')
    else:
        print(f'Убыток: {-balance:.2f}')

    if balance > 0:
        print(f'Рентабельность: {debet / credit * 100:.2f}%')

        staff = prompt_pos_int_number('Введите число сотрудников')
        if staff is not None:
            print(f'Прибыль на одного сотрудника: {balance / staff:.2f}')

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print('\n' + '-' * 20 + '\n')

distance = prompt_pos_number('Введите результат в первый день пробежки')
result = prompt_pos_number('Введите требуемый результат')

if distance is not None and result is not None:
    day = 1
    while True:
        print(f'{day}-й день: {distance}')
        if distance > result:
            break

        distance = round(distance * 1.1, 2)
        day += 1

    print(f'На {day}-й день спортсмен достиг результата — не менее {result} км.')
