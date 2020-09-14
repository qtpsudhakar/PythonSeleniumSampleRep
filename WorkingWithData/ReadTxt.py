f1 = open(r"C:\Users\envy\Desktop\PythonForTestersProject\Data\Demo.txt")
# print(f1.readlines())
while True:
    ln = f1.readline()

    if ln:
        print(ln)
    else:
        break