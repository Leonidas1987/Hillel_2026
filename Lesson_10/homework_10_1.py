from abc import ABC, abstractmethod


# =========================
# ЗАВДАННЯ 1
# =========================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


def test_teamlead_attributes():
    team_lead = TeamLead(
        "Leon",
        5000,
        "QA",
        "Python",
        5
    )

    assert hasattr(team_lead, "department")
    assert hasattr(team_lead, "programming_language")


# =========================
# ЗАВДАННЯ 2
# =========================

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Triangle(Figure):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.__base = base
        self.__height = height
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        return (self.__base * self.__height) / 2

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c


figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(4, 3, 3, 4, 5)
]

for figure in figures:
    print("Площа:", figure.area())
    print("Периметр:", figure.perimeter())
    print()