import sys

try:
    x=10
    print(x.x)
    y = 100
    print(x+y)
except:
    #record logs
#write results in to html
    print("failed",sys.exc_info())
    raise sys.exc_info()[0]
else:
    print("execute only if no exception")
finally:
    print("finally block")
