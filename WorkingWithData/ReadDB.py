from mysql import connector

con = connector.connect(host='localhost', port='3307', user='root', password='admin', database='company')
cr = con.cursor()
cr.execute('select * from emp') # insert / update query also accepted

data = cr.fetchall()
print(cr.column_names)

for id, name, age, sal in data:
    print(id, name, age, sal)
con.close()
