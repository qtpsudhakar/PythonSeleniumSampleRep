import sys
import os
def demoadd(a, b):
    return a + b

print(globals())
print(__name__)
if __name__ == '__main__':
    print(__name__)
    print(demoadd(2, 3))
    print('executed from Demo')
    print(globals())
    print(sys.path)
    # sys.path.append('')
    print(os.name)
    print(os.path)
    print(sys.exc_info())

