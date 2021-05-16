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
    

#! child of Student
#! herda name, school from class Student(Parent)
#? herda, atributos e métodos da class Parent

class WorkingStudent(Student):                   
    def __init__(self, name, school, salary):    
        
        super().__init__(name, school)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return self.salary * 35.50