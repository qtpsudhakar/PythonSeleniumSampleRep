users = ['sudhakar','balu',100,200,'balu']
print(len(users))
print(users[0])

print('sudhakar' in users)

users.append('indra')

print(users)
users.insert(8,'me')
print(users)
users.reverse()
print(users)
# del users
print(users.count('balu'))
users.clear()
print(users)

# tuple
data = (10,20,30,"sudhakar")
print(data)

print(len(data))

print(10 in data)

users=['sudhakar','balu','indra']
ages=[35,36,37]
nlst = users.copy() + ages.copy()

print(nlst)
# list is dynamic, duplicate values accepted, indexed, ordered