import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
    )

mycur=myconn.cursor()

mycur.execute("select * from customer")

results = mycur.fetchone()  #fetchall()

for i in results:
    print(i)


myconn.close()
