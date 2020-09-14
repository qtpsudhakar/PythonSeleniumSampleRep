class Employee:

    def __init__(self):
        self.__age = 25  # private variable

    @property
    def Age(self):  # getter method
        return self.__age

    @Age.setter
    def Age(self, age):  # setter method
        if age < 18:
            print('employee age must be greater than or equal 18')
        elif age > 65:
            print('employee age must be less than or equal 65')
        else:
            self.__age = age
            print('employee age updated:', self.__age)


e1 = Employee()
print(e1.Age)
e1.Age = 100
print(e1.Age)
e1.Age = 17
print(e1.Age)
e1.Age = 30
# read data will execute getter
# assign data will execute setter
# instance._classname__variable hack
