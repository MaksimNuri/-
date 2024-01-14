# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class ParquetBoard:
    def __init__(self, material: str, length: int, width: int):
        """
        Создание и подготовка к работе объекта "Паркетная доска"

        :param material: Материал паркетной доски
        :param length: Длина паркетной доски (в мм)
        :param width: Ширина паркетной доски (в мм)

        Примеры:
        >>> parquetboard = ParquetBoard("Сосна", 2000, 138)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

        if not isinstance(length, int):
            raise TypeError("Длина должна быть типа int")
        if length <= 0:
            raise ValueError("Длина должна быть больше 0")
        self.length = length

        if not isinstance(width, int):
            raise TypeError("Длина должна быть типа int")
        if width <= 0:
            raise ValueError("Длина должна быть больше 0")
        self.width = width

    def decrease_length(self, value: int) -> None:
        """
        Уменьшение длины паркетной доски

        :param value: На какую длину уменьшится паркетная доска
        :raise ValueError: Если длина на которую уменьшается длина доски больше первоначальной длины доски,
        то вызываем ошибку
        :return: Итоговая длина паркетной доски

        Примеры:
        >>> parquetboard = ParquetBoard("Сосна", 2000, 138)
        >>> parquetboard.decrease_length(200)
        """
        if not isinstance(value, int):
            raise TypeError("Длина, на которую уменьшается паркетная доска должна быть типа int")
        if value <= 0:
            raise ValueError("Длина, на которую уменьшается паркетная доска должна быть больше 0")
        ...

    def is_oak(self) -> bool:
        """
        Функция которая проверяет сделана ли паркетная доска из Дуба
        :return: Является ли материал из которого сделана паркетная доска дубом

        Примеры:
        >>> parquetboard = ParquetBoard("Сосна", 2000, 138)
        >>> parquetboard.is_oak()
        """
        ...


class Car:
    def __init__(self, color: str, weight: int, power: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param color: Цвет автомобиля
        :param weight: Вес автомобиля (в кг)
        :param power: Мощность автомобиля (в л.с)

        Примеры:
        >>> car = Car("Красный", 2454, 249)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight <= 0:
            raise ValueError("Вес должен быть больше 0")
        self.weight = weight

        if not isinstance(power, int):
            raise TypeError("Мощность должна быть типа int")
        if power <= 0:
            raise ValueError("Мощность должна быть больше 0")
        self.power = power

    def repaint(self, new_color: str) -> None:
        """
        Перекраска автомобиля в другой цвет
        :param new_color: Новый цвет автомобиля
        :return: Новый цвет автомобиля
        Примеры:
        >>> car = Car("Красный", 2454, 249)
        >>> car.repaint("Черный")
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет автомобиля должны быть типа str")
        ...

    def alleviation(self, new_weight: int) -> None:
        """
        Уменьшение веса автомобиля
        :param: new_weight: Новый вес автомобиля
        :raise ValueError: Если вес на который облегчили автомобиль, больше чем первичная масса автомобиля
        Примеры:
        >>> car = Car("Красный", 2454, 249)
        >>> car.alleviation(130)
        """
        if not isinstance(new_weight, int):
            raise TypeError("Вес, на который уменьшается масса автомобиля должнен быть типа int")
        if new_weight <= 0:
            raise ValueError("Вес, на который уменьшается масса автомобиля должен быть больше 0")
        ...


class Laptop:
    def __init__(self, memory: int, diagonal: (int, float), brand: str, ssd: int):
        """
        Создание и подготовка к работе объекта "Паркетная доска"

        :param memory: Оперативная память ноутбука (в Гб)
        :param diagonal: Диагональ ноутбука (в дюймах)
        :param brand: Марка ноутбука
        :param ssd: Объем SSD (в Гб)

        Примеры:
        >>> laptop = Laptop(8, 15.6, "Dell", 512)  # инициализация экземпляра класса
        """
        if not isinstance(memory, int):
            raise TypeError("Оперативная память должна быть типа int")
        if memory <= 0:
            raise ValueError("Оперативная память должна быть больше 0")
        self.memory = memory

        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ должна быть типа int или float")
        if diagonal <= 0:
            raise ValueError("Диагональ должна быть больше 0")
        self.diagonal = diagonal

        if not isinstance(ssd, int):
            raise TypeError("Объем SSD должен быть типа int")
        if ssd <= 0:
            raise ValueError("Объем SSD должен быть больше 0")
        self.ssd = ssd

        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        self.brand = brand
    def increase_memory(self, new_memory: int) -> None:
        """
        Увеличение оперативной памяти ноутбука
        :param: new_memory: Количество новой оперативной памяти
        Примеры:
        >>> laptop = Laptop(8, 15.6, "Dell", 512)
        >>> laptop.increase_memory(2)
        """
        if not isinstance(new_memory, int):
            raise TypeError("Память, на которую увеличивается общая оперативная память должан быть типа int")
        if new_memory <= 0:
            raise ValueError("Память, на которую увеличивается общая оперативная память должна быть больше 0")
        ...
    def increase_ssd(self, new_ssd: int) -> None:
        """
        Увеличение оперативной памяти ноутбука
        :param: new_memory: Количество новой оперативной памяти
        Примеры:
        >>> laptop = Laptop(8, 15.6, "Dell", 512)
        >>> laptop.increase_ssd(512)
        """
        if not isinstance(new_ssd, int):
            raise TypeError("Объем нового SSD должен быть типа int")
        if new_ssd <= 0:
            raise ValueError("Объем нового SSD должен быть больше 0")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
