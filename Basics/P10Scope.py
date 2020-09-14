x=10
def demo():

    global a
    a='hello'
    y=20
    z=100
    print(locals())
    global x # gives full access to global variable
    x=200
    print('value of x is',x)

demo()
for i in range(5):
    print(i)
print(globals())
print('latest value of x is ',x)
print(a)