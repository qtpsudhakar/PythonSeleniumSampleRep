import json

f1 = open(r"C:\Users\envy\Desktop\PythonForTestersProject\Data\Demo.json")

dt = json.load(f1)
dt["name"] = "qtpsudhakar"

f1.close()

f1 = open(r"C:\Users\envy\Desktop\PythonForTestersProject\Data\Demo.json",mode='w')

json.dump(dt,f1);
f1.close()
