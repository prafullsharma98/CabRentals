#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('customer.db')

print("Opened database successfully");

conn.execute('''CREATE TABLE CUSTOMER
         (FIRSTNAME CHAR(50)     NOT NULL,
         LASTNAME   CHAR(50)   NOT NULL,
         PHONENO    CHAR(20)    NOT NULL,
         EMAILID        TEXT,
         PASSWORD        CHAR(50));''')

print(" Customer Table created successfully");