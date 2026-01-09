import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

mycur = myconn.cursor()

insert_table_query = """
insert into customer(name, city)
values (%s, %s)
"""
query_data = [
    ('John Doe', 'New York'),
    ('Jane Smith', 'Los Angeles'),
    ('Mike Johnson', 'Chicago'),
    ('Emily Davis', 'Houston'),
    ('David Wilson', 'Phoenix')
]

mycur.executemany(insert_table_query, query_data)
myconn.commit()

print("Data inserted successfully")

myconn.close()


