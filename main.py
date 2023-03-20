class Student:
    """ Constructor """
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        print(f'{self.name} was successfully created!')

    def __str__(self):
        return f'I am {self.name}. I am {self.age} years old. I from {self.country}'

    def __del__(self):
        print(f'{self.name} was successfully deleted!')


# __init__ event
first_student = Student('Artur', 24, 'Ukraine')
second_student = Student('Vasya', 18, 'Poland')
third_student = Student('Petya', 20, 'Ukraine')
fourth_student = Student('Anna', 19, 'United Kingdom')

# __str__ event
print(first_student)
print(second_student)
print(third_student)
print(fourth_student)


# __del__ event
del first_student
del second_student
del third_student
del fourth_student