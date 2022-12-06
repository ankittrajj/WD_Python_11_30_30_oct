import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'alpha')

cursor = con.cursor()


query = "select * from emp"
cursor.execute(query)
data = cursor.fetchone()
# data = cursor.fetchmany()
# data = cursor.fetchall()
print(data)