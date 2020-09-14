
class Employee:
    company = 'python'
    def __del__(self):
        print('this is last')

    def __init__(self):
        self.age = 10
        self.name = 'abc'

    def getage(self):
        return self.age

    @staticmethod
    def demo():
        print('this is like function')


e1 = Employee()
e2 = Employee()
print(e1.age)
print(e2.age)

e1.age = 50
e2.age = 1000

print('e1 age', e1.age)# 100
print('e2 age', e2.age)# 100

print(Employee.company)
print(e1.company)
print(e2.company)

Employee.company = 'ibm'
print(e1.company)
print(e2.company)
# e1.company = 'oracle'

del e1
del e2