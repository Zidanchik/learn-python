
from abc import ABC, abstractmethod, abstractproperty

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix_data: list):
        if not matrix_data:
            raise ValueError('Пустое значение')

        self._rows = len(matrix_data)
        self._cols = None

        for i in matrix_data:
            if not isinstance(i, list):
                raise ValueError('Один из элементов не является списком')
            elif self._cols and len(i) != self._cols:
                raise ValueError('Разное количество элементов в строках')
            else:
                self._cols = len(i)

        self._matrix = matrix_data

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self._rows != self._rows or self._cols != self._cols:
                raise ValueError('Сложение матриц разных размерностей не поддерживается')

            # если поменять местами "for n in range(self._cols)" и "for m in range(self._rows)"
            # получится транспонированная матрица
            return Matrix([[self._matrix[m][n] + other._matrix[m][n] for n in range(self._cols)] for m in range(self._rows)])
        else:
            raise ValueError('Сложение типа Matrix с другими типами не поддерживается')

    def __str__(self):
        return '\n'.join(['Matrix:'] + [str(i) for i in self._matrix])


a = Matrix([[1, 1, 1], [2, 3, 4]])
b = Matrix([[5, 6, 7], [8, 8, 8]])
c = a + b

print(a)
print(b)
print(c)

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Dress(ABC):
    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @abstractmethod
    def calc_material(self):
        pass

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def __str__(self):
        return f'{self.name}, размер {self.size}'


class Topcoat(Dress):
    def __init__(self, size):
        super(Topcoat, self).__init__('Пальто', size)

    def calc_material(self):
        return 2 * self.size + 0.3


class Suit(Dress):
    def __init__(self, size):
        super(Suit, self).__init__('Костюм', size)

    def calc_material(self):
        return self.size / 6.5 + 0.5


print('\n' + '-' * 20 + '\n')

suit = Suit(32)
topcoat = Topcoat(12)

print(suit, f'требуется материала: {suit.calc_material():.3f}')
print(topcoat, f'требуется материала: {topcoat.calc_material():.3f}')

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение, объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток. Вычитание, участвуют две клетки. Операцию необходимо выполнять
# только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение, создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток. Деление, создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, cell_count: int):
        self.cell_count = cell_count

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError

        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError

        if other.cell_count > self.cell_count:
            print('Вычитание невозможно')
            return self
        else:
            return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError

        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError

        return Cell(round(self.cell_count / other.cell_count))

    def __str__(self):
        return f'Клетка. Ячеек: {self.cell_count}'


print('\n' + '-' * 20 + '\n')

cell1 = Cell(13)
cell2 = Cell(6)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
