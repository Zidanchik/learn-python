
from time import sleep, time
from enum import Enum


# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# (Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())

class TrafficLightSignals(Enum):
    RED_SIGNAL = {'color': 'Red', 'duration': 7}
    GREEN_SIGNAL = {'color': 'Green', 'duration': 15}
    YELLOW_SIGNAL = {'color': 'Yellow', 'duration': 2}


class TrafficLight:
    def __init__(self):
        self.__color = TrafficLightSignals.RED_SIGNAL

    def __switch(self):
        if self.__color is TrafficLightSignals.RED_SIGNAL:
            self.__color = TrafficLightSignals.YELLOW_SIGNAL
        elif self.__color is TrafficLightSignals.YELLOW_SIGNAL:
            self.__color = TrafficLightSignals.GREEN_SIGNAL
        else:
            self.__color = TrafficLightSignals.RED_SIGNAL

    def running(self, work_time=60):
        print(self.__color.value['color'])

        stop_time = int(time()) + work_time
        while time() < stop_time:
            sleep(self.__color.value['duration'])
            self.__switch()

            print(self.__color.value['color'])
            if int(time()) + self.__color.value['duration'] > stop_time:
                break


# TrafficLight().running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, mass_per_m2, thickness):
        return self._length * self._width * mass_per_m2 * thickness // 1000


print('\n' + '-' * 20 + '\n')

road = Road(5000, 20)

asphalt_mass = road.calc_asphalt_mass(25, 5)

print(f'Масса асфальта: {asphalt_mass} т')


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Иван', 'Иванов', 'Слесарь', 20000, 10000)

print('\n' + '-' * 20 + '\n')

print(position.get_full_name())
print(position.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Directions(Enum):
    RIGHT = 1
    LEFT = 2


class Car:
    def __init__(self, name, color, is_police=False):
        self.is_police = is_police
        self.color = color
        self.name = name
        self.__speed = 0

    def go(self, speed):
        self.set_speed(speed)
        print(f'Машина {self.name} поехала')

    def stop(self):
        self.set_speed(0)
        print(f'Машина {self.name} остановилась')

    def turn(self, direction: Directions):
        if direction is Directions.RIGHT:
            print(f'Машина {self.name} повернула направо')
        elif direction is Directions.LEFT:
            print(f'Машина {self.name} повернула налево')

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def show_speed(self):
        if self.__speed > 0:
            print(f'Машина {self.name} движется со скоростью {self.__speed} км/ч')
        else:
            print(f'Машина {self.name} не движется')


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.get_speed() > 60:
            print(f'Машина {self.name} превышает допустимую скорость')


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.get_speed() > 40:
            print(f'Машина {self.name} превышает допустимую скорость')


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


print('\n' + '-' * 20 + '\n')

town_car = TownCar('ВАЗ 21099', 'белая')
work_car = WorkCar('Газель', 'коричневая')
sport_car = SportCar('Ferrari', 'красная')
police_car = PoliceCar('Лада Веста', 'белая')

town_car.go(60)
work_car.go(60)
sport_car.go(200)
police_car.go(60)

town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()
police_car.show_speed()

town_car.turn(Directions.LEFT)
town_car.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки”.
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'Рисование ручкой')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'Рисование карандашом')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'Рисование маркером')


print('\n' + '-' * 20 + '\n')

item = Stationery('Кисть')
item.draw()

item = Pen()
item.draw()

item = Pencil()
item.draw()

item = Handle()
item.draw()
