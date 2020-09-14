import sys
try:
        eval('x=')

except Exception:
    try:
        print(sys.exc_info()[0])
        print('from except')
    except Exception:
        pass
finally:
    print('this is end')
