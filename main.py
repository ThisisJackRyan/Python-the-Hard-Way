class Parent(object):

    def __init__(self, name):
        self.name = name 
    def altered(self):
        print(f"Parent Altered() {self.name}")

class Child(Parent):
    def __init__(self, name):
        self.name = name 
    def altered(self):
        print(f"child, before parent altered() {self.name}")
        super(Child, self).altered()
        print(f"Child, after Parent altered() {self.name}")


dad = Parent("John")
son = Child("Jack")

dad.altered()
son.altered()