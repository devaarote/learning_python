import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
    )

mycur=myconn.cursor()

alter_table_query = "ALTER TABLE STUDENTS ADD COLUMN id int unique auto_increment primary key;"

mycur.execute(alter_table_query)

print("Table altered successfully")



myconn.close()