import json

jst = '{"name":"John", "age":31, "city":"New York"}'

dt = json.loads(jst)
print(dt['name'])

dt['name']="sudhakar"
print(dt)