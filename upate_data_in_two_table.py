import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",    
    database="testdb"
)

mycur=myconn.cursor()

mycur.execute("""CREATE TABLE user(id int primary key ,name varchar(20),fav int)""")

mycur.execute("""CREATE TABLE vehical(id int primary key ,vehical_name varchar(20))""")

user_values=[(1,'remma',154),(2,'vishal',178),(3,'ajay',189),(4,'suresh',None),(5,'kumar',None)]

mycur.executemany("insert into user values(%s,%s,%s)",user_values)

vehical_values=[(1,'car'),(2,'bike'),(3,'bus'),(4,'truck'),(5,'cycle')]

mycur.executemany("insert into vehical values(%s,%s)",vehical_values)

myconn.commit()

print("data inserted successfully in both tables")  

mycur.close()
myconn.close()

