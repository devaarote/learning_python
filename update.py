import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"

)
mycur = myconn.cursor()

record_city= 'phoenix'


print("Before updating data")
mycur.execute("select * from customer where name=%s", (record_city,))
before_update = mycur.fetchone()

print(before_update)

update_query = "update customer set name=%s where city=%s"
new_data= ('Vishal',record_city)
mycur.execute(update_query, new_data)
myconn.commit()

print("After updating data")
mycur.execute("select * from customer where city=%s", (record_city,))
after_update = mycur.fetchone() 

print(after_update)
myconn.close()
