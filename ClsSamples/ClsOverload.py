
class demomaths:
    def demoadd(self,a,b):
        return a+b

class demomaths1(demomaths):
    def demoadd(self, a, b,c=None):
        if c==None:
            return super().demoadd(a,b)
        else:
            return a+b+c
    def f1(self):
        pass
class demo(demomaths1):
    # pass
    def demoadd(self):
        print('demo add called')
dm = demomaths1()
print(dm.demoadd(2, 3))
print(dm.demoadd(2, 3,4))

d1 = demo()
d1.demoadd()
d1.f1()

print(isinstance(dm, demo))

