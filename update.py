import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'alpha')

cursor = con.cursor()

name = input("Enter your name")
# age = int(input("Enter your age"))
sal = int(input("Enter your salary"))

query = "Update emp set name = '{}' where sal = {}".format(name,sal)
cursor.execute(query)
con.commit()
print("Data entered successfully!!")

# on the basis of age chnage the salary.