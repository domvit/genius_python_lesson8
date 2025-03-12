# Завдання 2: Абстракція
#
# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний
# метод "обчислити_площу" (calculate_area).
#
# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle),
# "Прямокутник" (Rectangle) і "Трикутник" (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу"
# відповідно до формули для обчислення площі кожної фігури.
#
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Абстрактний метод для обчислення площі"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Обчислює площу кола: pi * r^2"""
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Обчислює площу прямокутника: ширина * висота"""
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        # Перевірка валідності трикутника (сума любих двох сторін більша за третю)
        if not (side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2):
            raise ValueError("Такий трикутник не існує!")

    def calculate_area(self):
        """Обчислює площу трикутника за формулою Герона"""
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(side1=3, side2=8, side3=7)

print(f"Площа кола: {circle.calculate_area():.2f}")
print(f"Площа прямокутника: {rectangle.calculate_area()}")
print(f"Площа трикутника: {triangle.calculate_area()}")