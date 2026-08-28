class Student:
    """Клас, що представляє студента."""

    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_average_grade):
        """Змінює середній бал студента."""
        self.average_grade = new_average_grade

    def show_info(self):
        """Виводить інформацію про студента."""
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")


student = Student("Leon", "Fon", 39, 77)

print("До зміни середнього балу:")
student.show_info()

student.change_average_grade(95)

print("\nПісля зміни середнього балу:")
student.show_info()