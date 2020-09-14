class Employee:

    def __init__(self):
        self.__age = 25 # private variable
    def getAge(self): # getter method
        return self.__age
    def setAge(self,age): # setter method
        if age<18:
            print('employee age must be greater than or equal 18')
        elif age>65:
            print('employee age must be less than or equal 65')
        else:
            self.__age = age
            print('employee age updated:',self.__age)
e1 = Employee()
# e1.__age = 1000
# print(e1.__age)
print(e1.getAge())
e1.setAge(17)
print(e1.getAge())
e1.setAge(66)
print(e1.getAge())
e1.setAge(30)
print(e1.getAge())

print(e1._Employee__age) # hack


