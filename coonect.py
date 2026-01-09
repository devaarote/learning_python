import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

mycur = myconn.cursor()

sql = """
SELECT user.name AS user_name, vehical.vehical_name AS favorite
FROM user
INNER JOIN vehical ON user.fav = vehical.id
"""

mycur.execute(sql)  
result = mycur.fetchall()

for i in result:
    print(i)


mycur.close()
myconn.close()

