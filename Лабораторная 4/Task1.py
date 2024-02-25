if __name__ == "__main__":
    class Transport:
        """Базовый класс для транспортных средств."""

        def __init__(self, color: str):
            """Инициализация транспортного средства с указанием цвета."""
            self._color = color

        def move(self) -> str:
            """Абстрактный метод движения транспортного средства."""
            raise NotImplementedError("Метод move должен быть переопределен в дочерних классах")

        def get_color(self) -> str:
            """Получить цвет транспортного средства."""
            return self._color

        def __str__(self) -> str:
            """Строковое представление транспортного средства."""
            return f"Транспортное средство цвета {self._color}"

        def __repr__(self) -> str:
            """Представление транспортного средства."""
            return f"{self.__class__.__name__}(цвет={self._color})"


    class Car(Transport):
        """Дочерний класс для автомобилей."""

        def __init__(self, color: str, brand: str):
            """Инициализация автомобиля с указанием цвета и марки."""
            super().__init__(color)
            self._brand = brand

        def move(self) -> str:
            """Движение автомобиля."""
            return f"{self._brand} едет по дороге"

        def __str__(self) -> str:
            """Строковое представление автомобиля."""
            return f"Автомобиль марки {self._brand} цвета {self.get_color()}"


    class Bicycle(Transport):
        """Дочерний класс для велосипедов."""

        def __init__(self, color: str, type: str):
            """Инициализация велосипеда с указанием цвета и типа."""
            super().__init__(color)
            self._type = type

        def move(self) -> str:
            """Движение велосипеда."""
            return "Велосипед едет по дороге"

        def __str__(self) -> str:
            """Строковое представление велосипеда."""
            return f"Велосипед типа {self._type} цвета {self.get_color()}"
    pass
