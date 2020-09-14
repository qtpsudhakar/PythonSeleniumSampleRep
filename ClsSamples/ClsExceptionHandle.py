import sys
try:
    # a=
    print(z)
    x=10
    print(x.x)
    y=100
    print(x+y)
except NameError:
    # record logs
    # write results in to html
    print('failed because variable not initialized')
    # print('execution completed')
    print(sys.exc_info())
    raise sys.exc_info()[1]
except AttributeError:
    print('failed because attribute not exist for the given reference')
    raise sys.exc_info()[0]
except Exception:
    print('failed due to error')
    raise sys.exc_info()[0]
# create results, logs, screenshots
else:
    print('execute only if no exception')
finally:
    print('post condition executed')
# try if exception occurs except block will be executed
# irrespective exception occurs or not finally will be executed