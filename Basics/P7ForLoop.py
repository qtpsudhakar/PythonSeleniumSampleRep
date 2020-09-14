# print(list(range(1,10)))

# print numbers from 1 to 10

for i in range(11):
    print(i)

# print odd numbers between 10 and 30
for i in range(10,31):
    if i%2==1:
        print(i)

# print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

for i in reversed(range(1,11)):
    print(i)

# print values of a list
lst = [10,20,30]
for v in lst:
    print(v)

# print list values using index
for i in range(len(lst)):
    print(lst[i])

# program for prime number
n = 1
for i in range(2,n):
    if n%i==0:
        print(n,' is not a prime number')
        break
else:
    print(n, ' is a prime number') if n !=1 else print(n,' is not a prime number')

# print string in reverse
tool = 'selenium'
for i in reversed(tool): print(i)

[print(i) for i in tool]