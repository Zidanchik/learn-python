from collections import Counter
from functools import reduce

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор списка.
#
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = [v for i, v in enumerate(lst) if i > 0 and lst[i - 1] < v]

print(lst)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор списка.

print('\n' + '-' * 20 + '\n')

print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор списка.
# (Можно использовать list.count()).
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

print('\n' + '-' * 20 + '\n')

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# первый вариант
print([i for i in lst if lst.count(i) == 1])

# второй вариант
print([k for k, v in Counter(lst).items() if v == 1])

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().

print('\n' + '-' * 20 + '\n')

lst = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x * y, lst))

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
# На вебинаре реализовали похожий пример для чисел Фиббоначи.

print('\n' + '-' * 20 + '\n')


def fact(n: int):
    if n == 0:
        yield 1

    f = 1
    for i in range(1, abs(n) + 1):
        f *= i
        yield f if n > 0 else -f


for el in fact(-4):
    print(el)
