
def smartAdd(f):
    def smart(n1,n2):
        if type(n1)==int and type(n2)==int:
            return n1+n2
        elif type(n1)==str or type(n2)==str:
            return f'{n1}{n2}'
    return smart

@smartAdd
def demoadd(a,b):
    return a+b

print(demoadd(2, 3))
print(demoadd("hello","how are you"))
print(demoadd("hello",10))
print(demoadd(10,"20"))
# print(smartAdd("selenium","webdriver"))
