#%%
my_student = {
    'name'    : 'Fabio Lima',
    'grades'  : [70, 88, 90, 99], 
    'average' :  None # something here like a function to calculate the average
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    """[Uma classe que modela um objeto tipo estudante com 2 atributos]
    """    
    def __init__(self, new_name, new_grade):
        """[dunder method: init para a classe Student]
        Args:
            new_name ([string]): [nome do aluno - atributo]
            new_grade ([lista]): [lista com as notas do atributo name]
        """
        self.name = new_name
        self.grades = new_grade
    
    
    def __str__(self) -> str:
        """[string representation for the user]
        Returns:
            [type]: [description]
        """        
        return f"<Student: {self.name}, Grades: {self.grades}>"

    def average(self):
        return sum(self.grades) / len(self.grades)


#! criação  de instâncias da classe Student
fabio = Student('Fabio Lima', [70, 88, 95, 99])
fabiana = Student('Fabiana Oliveira', [100, 90, 77, 89])

print(fabio.name)
print(fabiana.name)
print(f"A média das notas do aluno {fabio.name} é {fabio.average()}")
print(type(fabio))  #! qdo printamos o tipo(isto é a classe de um objeto)
print(fabio)        #! qdo fizemos print(type(fabio)), Python returns the type
                    #! and the memory location of the object.

# %%
movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)
# %%
