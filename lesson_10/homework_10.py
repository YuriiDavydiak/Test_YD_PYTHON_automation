# Task 1

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )

team_lead = TeamLead("Yurii", 10000, "AQA", "Python", 5)

print(team_lead.name)
print(team_lead.salary)
print(team_lead.department)
print(team_lead.programming_language)
print(team_lead.team_size)

# Task 2

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Rhombus(Shape):
    def __init__(self, side, height):
        self.__side = side
        self.__height = height

    def area(self):
        return self.__side * self.__height

    def perimeter(self):
        return 4 * self.__side


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Rhombus(3, 4)
]


for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")