x=20
y=20
# find which is bigger
if x>y:
    print('x is bigger')
elif x<y:
    print('y is bigger')
else:
    print('both are equal')

# find odd number
n = 10
if n%2==1:
    print(n,' is odd number')
else:
    print(n,' is even number')

print(n,' is odd number') if n%2==1 else print(n,' is even number')
print('x is bigger') if x>y else print('y is bigger') if x<y else print('both are equal')

