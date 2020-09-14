
# class members : can be accessed using classname
# instance members : can be accessed only with instance
# by using instance we can access class members
class Employee:
    age=10 # class variable
    def __init__(self): # constructor
        self.age = 50
        print('constructor method executed')

    def getAge(self): # instance method
        print(self.age)
    def demoadd(self,a,b): # instance method
        return a+b
    @classmethod
    def printempage(cls):
        print(cls.age)

print('classvar:',Employee.age)
# print(Employee.getAge())
# classname() will create an instance
# By using instance we can acces the members of the class
# e1 having instance of class
# e1 reffering employee
e1 = Employee()
e1.getAge()
print(e1.age)
Employee.getAge(e1)
print(Employee.demoadd(e1, 10, 20))
Employee().getAge()

e2 = Employee()
e2.getAge()
print('classvar:',Employee.age)
Employee.printempage()