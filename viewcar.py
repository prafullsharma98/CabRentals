import sqlite3

conn = sqlite3.connect('car.db')
print("Opened database successfully");

cursor = conn.execute("SELECT * from CAR")
for row in cursor:
	print(str(row[5]))



# print(s)
conn.close()