import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    )

mycur=myconn.cursor()

mycur.execute("show databases")

for i in mycur:
    print(i)


myconn.close()