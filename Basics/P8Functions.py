# find odd number function
def findodd(n):
    if n % 2 == 1:
        print(n, ' is odd number')
    else:
        print(n, ' is even number')


findodd(10)
findodd(11)
findodd(15)


def demoadd(a, b):
    print(a + b)


demoadd(2, 3)

demoadd(2, 30)


def isOdd(n):
    if n % 2 == 1:
        return True
    else:
        return False


print(isOdd(10))


def getaddition(a, b):
    return a + b


# default parameters
def login(uname='admin', pwd='asdf'):
    print(f'logged into application using {uname} and {pwd}')


login()
login('guest', 'qwer')
login('guest')


def applogin(uname, pwd):
    print(f'logged into application using {uname} and {pwd}')


applogin('admin', 'asdf')  # positional
applogin(pwd='zxcv', uname='guest')  # keyword

applogin('guest', pwd='zxcv')


# applogin('guest',uname='zxcv')

def addvalues(*v):  # accepts unlimited positional args
    print(type(v))
    print(sum(v))
    print(v)


lst = [10, 20, 30, 40]
addvalues(*lst)


def printvalues(**v):  # accepts unlimited keyword args
    print(type(v))
    print(v)
    print(sum(v.values()))


printvalues(x=10, y=20)

# def fn():pass
# return
# def fn(a,b,c):pass
# positional, keyword args

def alogin(*,uname, pwd):
    print(f'logged into application using {uname} and {pwd}')

alogin(uname='admin',pwd='asdf')
alogin('admin','asdf')

def testp(p1,p2,/,n1,n2,*,k1,k2):pass

#how many positional arguments will testp function accept
#yes 2 : wrong
#no 4

#how many keyword arguments will testp function accept


