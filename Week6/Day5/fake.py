import sqlite3 as sl
from faker import Faker
from time import time

f = Faker()

connection = sl.connect("fake-data.db")

cursor = connection.cursor()

start = time()

for i in range(100000):
    query = f"INSERT INTO people (name, email) VALUES ('{f.name()}', '{f.email()}')"
    cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end - start)