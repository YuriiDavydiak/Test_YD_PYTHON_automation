class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def get_info(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Grade: {self.average_grade}"



student = Student("Yurii", "Davydiak", 49, 98)

print(student.get_info())

student.update_average_grade(100)

print(student.get_info())

