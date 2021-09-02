#! HERANÇA
class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def __repr__(self) -> str:
        return f"<< Student: {self.name}, School: {self.school} >>"

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def info_class(cls):
        print(cls.__name__)

    @staticmethod
    def hi():
        print('I there, I dont take any parameter at all')


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 35.50


student1 = Student('Fabio Lima', 'UNIPE')
student1.info_class()
student1.hi()
