class Parent(object):
    
    def altered(self):
        print("Parent Altered()")

class Child(Parent):

    def altered(self):
        print("child, before parent altered()")
        super(Child, self).altered()
        print("Child, after Parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()