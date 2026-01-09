import mysql.connector

myconn=mysql.connector.connect(
    host="localhost"
    ,user="root",
    password="root",
    database="testdb"
    )

mycur=myconn.cursor()

create_table_query = """CREATE TABLE STUDENTS(
name varchar(20) not null,
dept varchar(50),
roll_no int primary key not null,
section varchar(10),
age int
);"""

mycur.execute(create_table_query)
print("Table created successfully")

myconn.close()