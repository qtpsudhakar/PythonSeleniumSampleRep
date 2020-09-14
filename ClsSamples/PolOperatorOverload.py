# Called as dunder methods or magic methods

class Student:
    def __len__(self):
        return 10
    def __str__(self):
        return 'Student'
    def demo(self):
        print('demo called')
s1 = Student()
print(len(s1))
print(str(s1))
