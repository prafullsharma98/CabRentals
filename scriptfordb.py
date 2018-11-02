import cgi, cgitb 
import sqlite3

conn = sqlite3.connect('customer.db')

conn.execute("create table Query (email text,name text,query text);")

conn.close()