class Student:
    """[Define a Student class that has name and grade as properties]
    """
    def __init__(self, name, school):
        """[dunder method: init para a classe Student]
        Args:
            name ([string]): [name of the student]
            school ([list]): [school where the student go]
        """
        self.name = name
        self.school = school
        self.marks = []

    def __str__(self) -> str:
        """[string representation for the user]
        Returns:
            [type]: [description]
        """
        return f"<Student: {self.name}, Grades: {self.marks}>"

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
