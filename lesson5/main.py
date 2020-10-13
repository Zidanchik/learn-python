
import re
import json

from random import randint


def get_num_ending(num: int, default_word, word_for_1=None, word_for_2_4=None):
    word_for_1 = word_for_1 or default_word
    word_for_2_4 = word_for_2_4 or default_word

    last_digit = num % 10
    if last_digit == 0 or last_digit > 4 or num in range(11, 20):
        return default_word
    elif last_digit == 1:
        return word_for_1
    else:
        return word_for_2_4


# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('file.txt', mode='w', encoding='utf-8') as f:
    while True:
        text = input('Введите текст: ')
        if not text:
            break

        f.write(text + '\n')

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

print('\n' + '-' * 20 + '\n')

line_count = 0
total_word_count = 0

with open('file2.txt', encoding='utf-8') as f:
    for line in f:
        line_count += 1
        word_count = len(line.split())
        total_word_count += word_count

        word_count_text = get_num_ending(word_count, 'слов', 'слово', 'слова')

        print(f'Строка {line_count}: {word_count} {word_count_text}')

line_count_text = get_num_ending(line_count, 'строк', 'строка', 'строки')
word_count_text = get_num_ending(total_word_count, 'слов', 'слово', 'слова')

print(f'Итого: {line_count} {line_count_text}, {total_word_count} {word_count_text}')

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

print('\n' + '-' * 20 + '\n')

salary_of_staff = {}
with open('file3.txt', encoding='utf-8') as f:
    for line in f:
        employee, salary = line.split()

        salary_of_staff[employee] = float(salary)

for key, value in salary_of_staff.items():
    if value < 20000:
        print(key)

avg_salary = sum([i for i in salary_of_staff.values()]) / len(salary_of_staff)
print(f'Средняя величина дохода: {avg_salary:.2f}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

with open('file4.txt', encoding='utf-8') as in_file, open('file4_new.txt', 'w', encoding='utf-8') as out_file:
    for line in in_file:
        word, hyphen, num = line.split()

        new_word = num_dict[word.lower()].capitalize()

        new_line = f'{new_word} - {num}\n'

        out_file.write(new_line)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print('\n' + '-' * 20 + '\n')

# sum_of_nums = 0
with open('file5.txt', 'w') as f:
    for i in range(100):
        num = randint(1, 100)
        # sum_of_nums += num
        f.write(str(num) + ' ')

# print(f'Сумма: {sum_of_nums}')

# первый вариант, малый объем данных
with open('file5.txt') as f:
    content = f.read().split()

sum_of_nums = sum(map(int, content))
print(f'Сумма: {sum_of_nums}')

# второй вариант, большой объем данных в одной строке
chunk_size = 100
sum_of_nums = 0
piece = ''

with open('file5.txt') as f:
    chunk = f.read(chunk_size)
    while chunk:
        nums = chunk.split()

        if piece and not chunk[0].isspace():
            piece += nums.pop(0)
            sum_of_nums += int(piece)
            piece = ''

        if not chunk[-1].isspace():
            piece = nums.pop()

        sum_of_nums += sum(map(int, nums))

        chunk = f.read(chunk_size)

    if piece:
        sum_of_nums += int(piece)

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

print('\n' + '-' * 20 + '\n')

lectures = {}
with open('file6.txt', encoding='utf-8') as f:
    for line in f:
        name, lessons = line.split(':')

        lessons = [re.findall(r'\d+', i) for i in lessons.split()]
        lessons = sum([int(i[0]) if i else 0 for i in lessons])

        lectures[name.strip()] = lessons

for key, value in lectures.items():
    print(key, value, sep=': ')

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

avg_profit_count = 0
total_profit = 0
lst = [{}]

with open('file7.txt', encoding='utf-8') as f:
    for line in f:
        name, form, profit, expense = line.split()

        profit = float(profit)
        expense = float(expense)

        income = profit - expense
        if income > 0:
            avg_profit_count += 1
            total_profit += income

        lst[0][name.strip()] = income

lst.append({'average_profit': round(total_profit / avg_profit_count * 10) / 10})

with open('file7_out.txt', 'w', encoding='utf-8') as f:
    json.dump(lst, f)
