
def counter():
    i=0
    def count():
        nonlocal i
        i = i+1
        return i
    return count

add = counter()

print(add())
print(add())
print(add())
print(add())
print(add())

