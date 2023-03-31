#I chose exercise1


class Cat:
    def __init__(self, name, age, view, height, weight):
        self.name = name
        self.age = age
        self.view = view
        self.height = height
        self.weight = weight
    def __str__(self):
        return f'This is {self.name}. Her age is {self.age}. She is from {self.view}. Her height {self.height}, weight {self.weight}.'


first_cat = Cat('Lizy', 2, 'lynx', 30, 3)
second_cat = Cat('Cassy', 2, 'american',20, 3)


print(first_cat)
print(second_cat)
