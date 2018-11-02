#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('customer.db')

print("Opened database successfully");

conn.execute('''CREATE TABLE CAR
         (ID CHAR(50) PRIMARY KEY    NOT NULL,
         BRAND   CHAR(50)   NOT NULL,
         MODEL    CHAR(20)    NOT NULL,
         SEATER       INT,
         PRICEPERDAY       INT,
         URL        CHAR(500));''')

print(" CarTable created successfully");

conn.execute("INSERT INTO CAR \
      VALUES (3, 'Ford','eco-sport',5,1000,'https://www.toddjudyfordeast.com/inventoryphotos/4996/maj6p1ul5jc215279/sp/1.jpg')");

print("recs enetered")
conn.commit()
conn.close()