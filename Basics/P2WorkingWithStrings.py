user = 'sudhakar'

# wl = "hi"+user+", how are you"
wl = "hi{}, how are you".format('sudhakar')

wl = f"hi{user}, how are you" # formatted string
print(wl)

fldPath = r'c:\test' # \t represents tab \n new line
print(fldPath)

# raw string , formmatted string

hello = '$'
xxxx = f"how are you {hello}"
print(xxxx)

print('sudhakar'[2:])

del hello,fldPath
# print(hello)
fldPath=None
print(fldPath)

# formatting

# msg = 'hi {}, how are you'
# print(msg.format('sudhakar'))
msg = 'hi %s, how are you %i'
print(msg % ('sudhakar',10))
# f: float, i, d: numbers, r: raw

msg = 'hi {1}, how are you {0}'
print(msg.format('sudhakar','balu'))

print('i' in 'sudhakar') # verify string exist in other
s1 = 'sudhakar'
print(s1.index('u'))# gives error if sub string not exist
print(s1.find('i')) # gives -1 if sub string not exist
