def demo(a, b):
    return a + b


x = demo
print(x)
y = x(10, 20)
print(y)

z = demo(1, 2)
print(z)


def demomaths(a,b,act):
    if act=='add':
        return a+b
    if act=='mul':
        return a*b


print(demomaths(10, 20, 'add'))
print(demomaths(10, 20, 'mul'))

def demomathsf(a,b,act):
    return act(a,b)

def demoadd(a,b):
    return a+b

def demomul(a,b):
    return a*b


print(demomathsf(2, 3, demoadd))
print(demomathsf(2, 3, demomul))
print(demomathsf(2, 3, lambda a,b:a/b))

lst = [10,20,30,40,50]

def eq(n):
    return n>30
eq1 = lambda n:n>30
print(list(filter(lambda n:n>30, lst)))

print(list(map(lambda n: n +2, lst)))
# lambda parameters:expression
