class Person:

    #initializer/constructor
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self,newName):
        self.name = newName

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True


#RUNNING CODE
e = Person("Diana") #an object or an instance of a Person

e2=Employee("Anah") #an object/instance of an Employee

print(e.getName())
print(e.isEmployee())

print(e2.getName())
print(e2.isEmployee())

e.setName("Moana")
print(e.getName())
