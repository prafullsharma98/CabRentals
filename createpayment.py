#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('customer.db')

print("Opened database successfully");

# conn.execute('''CREATE TABLE PAYMENT
#          (PID INTEGER PRIMARY KEY AUTOINCREMENT,
#          NAME TEXT,
#          EMAILID TEXT,
#          CARID INTEGER,
#          FROMDATE TEXT,
#          TODATE TEXT,
#          DAYS TEXT,
#          ADDRESS TEXT,
#          STATE TEXT,
#          PICKUPTIME TEXT,
#          DROPOFFTIME TEXT,
#          PAY REAL);''')

# conn.commit()
# print(" payTable created successfully");

name="rikaaa"
emailid="tanujm@gmail.com"
fromdate="2018-11-19"
todate="2018-11-29"
days="10"
address="srinagar"
state="jammu and kashmir"
ptime="5:30"
dtime="8:45"
pay="70000"
carid="6"

conn.execute("INSERT INTO PAYMENT(NAME,EMAILID,CARID,FROMDATE,TODATE,DAYS,ADDRESS,STATE,PICKUPTIME,DROPOFFTIME,PAY) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(name,emailid,carid,fromdate,todate,days,address,state,ptime,dtime,pay))
conn.commit()


print("recs enetered babay ")

conn.close()