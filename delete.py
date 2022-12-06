import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'alpha')

cursor = con.cursor()

# name = input("Enter your name")
age = int(input("Enter your age"))
# sal = int(input("Enter your salary"))

query = "delete from emp where age = {}".format(age)
cursor.execute(query)
con.commit()
print("Data entered successfully!!")