# not like other languages
# achieve it using default parameters

from multipledispatch import dispatch

class demomaths:
    @dispatch(int, int)
    def demoadd(self,a,b):
        return a+b

    @dispatch(int, int,int)
    def demoadd(self,a,b,c):
        return a+b+c
class demomaths1(demomaths):

    @dispatch(int, int)
    def demoadd(self, a, b):
        return a - b

dm = demomaths()
print(dm.demoadd(2, 3))
print(dm.demoadd(2, 3,4))

dm1 = demomaths1()
print(dm1.demoadd(20, 30))
# print(dm1.demoadd(20, 30,40)) #Error
