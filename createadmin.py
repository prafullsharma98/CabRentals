#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('admin.db')

print("Opened database successfully");

conn.execute('''CREATE TABLE ADMIN
         (ADMINID INT PRIMARY KEY    NOT NULL,
         PASSWORD       CHAR(50));''')

# print(" CarTable created successfully");

conn.execute("INSERT INTO ADMIN \
      VALUES (1000, 'admin123')");

conn.commit()