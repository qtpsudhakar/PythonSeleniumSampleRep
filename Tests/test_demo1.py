from config import logger as log
def demoadd(a,b):
    log.info("i am in demo add method")
    return a+b

def test_demoadd1():
    log.info("i am in test_demoadd1")
    print('first')

def test_demoadd3():
    print('third')

def test_demoadd2():
    print('second')


