class Student:
    def __init__(self):
        self.name = ""
        self.__full_name = ""
        self.age = ""

    def display(self):
        print(f"Student Name is {self.name} and his age is {self.age} and full_name = {self.__full_name}")


class Teacher:

    def __init__(self):
        self.name = ""
        self.__full_name = ""
        self.age = ""

    def display(self):
        print(f"Teacher Name is {self.name} and his age is {self.age} and full_name = {self.__full_name}")


class ClassRoom(Student, Teacher):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.__full_name = ""

    def display(self):
        print(f"Class Name is {self.name} and full_name = {self.__full_name}")


a = ClassRoom()
a.name = "2/5"
a._Student__name = "Ahmed"
a._Teacher__name = "Seif"
a.full_name = "2/5"
a._Student__full_name = "Ahmed"
a._Teacher__full_name = "Seif"
a.full_name = "Moder School"
Student.display(a)
Teacher.display(a)
a.display()
print(a.__dict__)


