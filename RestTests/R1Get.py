from jsonpath_ng import jsonpath, parse
import requests

resp = requests.get("https://reqres.in/api/users/2")
print(resp)
print(resp.status_code)
print(resp.text)
print(resp.json())

je = parse('data.email')
res = je.find(resp.json())
print(res)
print(res[0].value)

p = requests.post('https://reqres.in/api/users',data={"name":"morpheus","job": "leader"})
print(p.text)
print(p.status_code)