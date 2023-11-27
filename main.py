class Animal(object):

    pass

class Dog((Animal)):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

    
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class fish(object):
    pass

class Salmon(fish):
    pass
class Halibut(fish):
    pass


rover = Dog("Rover")
satan = Cat("Satan")
mary = Dog("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = fish()

crouse = Salmon()

harry = Halibut()