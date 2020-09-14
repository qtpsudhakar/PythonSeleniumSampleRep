# [],(),{}

# set is dynamic, No duplicate values accepted, not indexed, not ordered
nu = {'selenium',20,10,20,30,10,20,10,20,"sudhakar"}

print(nu)

nu.update((10,20,30,50,100)) # update multiple values to set

print(nu)
lnu = list(nu)
print(lnu[0])


userdata ={'name':'sudhakar','job':'architect'}

print(userdata["name"])
userdata['othername'] = 'qtpsudhakar'
print(userdata)

print(userdata.get('othername'))
userdata.update({'age':35,'company':'fleelancer'})
print(userdata)
# dynamic , ordered, indexed, duplicate values accepted

userdata ={"name": "sudhakar", "job": "architect",None:'test'}
print(userdata.values())
