#!"C:\Users\Mahe\Anaconda3\python.exe"
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3

#conn = sqlite3.connect('name.db')

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

conn = sqlite3.connect('customer.db')



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>cars</title>")

s1="#customers{"

s1+="font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;"
s1+="border-collapse: collapse;"
s1+="width: 100%;}"
s1+="#customers td, #customers th {"
s1+="border: 1px solid #ddd;"
s1+="padding: 8px;}"

s1+="#customers tr:nth-child(even){background-color: #f2f2f2;}"

s1+="#customers tr:hover {background-color: #ddd;}"
s1+="#customers th {"
s1+= "padding-top: 12px;"
s1+="padding-bottom: 12px;"
s1+="text-align: left;"
s1+="background-color: #4CAF50;"
s1+="color: white;}"
s1+="h2{ text-align:center;}"
print("<style>%s</style>" % (s1,))



# print("<link rel='stylesheet' type='text/css' href='carview.css'>")
print("</head>")
print("<body>")

print("<h2>Select A Car</h2>")
print("<button><a href='http://localhost/main.html'>go back</a></button>")
s="<table id='customers' border='1' cellspacing='0' cellpadding='10px'>"
s+="<tr><th>car id</th> <th>Brand</th><th>Model</th><th>seater</th><th>price per day</th><th>image</th></tr>"
cursor = conn.execute("SELECT * from CAR")

for row in cursor:
	s+="<tr>"
	s+="<td>"+str(row[0])+"</td><td>"+str(row[1])+"</td>"+"<td>"+str(row[2])+"</td><td>"+str(row[3])+"</td>"+"<td>"+str(row[4])+"</td>"
	s+="<td>"+"<img height='250px' width='400px' src='"+str(row[5])+"'></td></tr>"


s+="</table>"

print("<p> %s </p>" % (s,))  

conn.close()
# print("""<a href="https://www.google.com" id="za"> Click me </a>""")
# print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

print("</body>")
print("</html>")