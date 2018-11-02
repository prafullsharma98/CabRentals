#!"C:\Users\Mahe\Anaconda3\python.exe"
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3
import time

#conn = sqlite3.connect('name.db')

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
adminid  = form.getvalue('id')
pwd = form.getvalue('pwd')


conn = sqlite3.connect('admin.db')



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>")
print("<title>admin-stats</title>")
print("</head>")
print("<body>")

i=0
flag=False
cursor = conn.execute("SELECT PASSWORD from ADMIN where ADMINID=?",(adminid,))
for row in cursor:
	if pwd==row[0]:
		flag=True
	i+=1	

if i==0 :
	print("<h2>No such name<h2>")

else :
	if flag==False:
		print("<h2>login unsuccessful</h2>")
		print("""<a href="http://localhost/adminlogin.html"> try again </a>""")	
	else:
		print("<h2>login successful</h2>")
		print("""<a href="http://localhost/adminoptions.html" id="za"> Click me </a>""")
		print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

		




conn.close()
# print("""<a href="https://www.google.com" id="za"> Click me </a>""")
# print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

print("</body>")
print("</html>")