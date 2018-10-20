#!"C:\Users\Mahe\Anaconda3\python.exe"
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3

#conn = sqlite3.connect('name.db')

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('fname')
last_name  = form.getvalue('lname')
phoneno = form.getvalue('phoneno')
emailid  = form.getvalue('email')
password  = form.getvalue('paswd')


conn = sqlite3.connect('customer.db')

conn.execute("INSERT INTO CUSTOMER  \
      VALUES (?,?,?,?,?)",(first_name,last_name,phoneno,emailid,password));

conn.commit()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Stats</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))

s="<table border='1' cellspacing='0' cellpadding='10'>"
cursor = conn.execute("SELECT FIRSTNAME,LASTNAME,PHONENO,EMAILID,PASSWORD from CUSTOMER")
for row in cursor:
	s+="<tr>"
	s+="<td>"+str(row[0])+"</td>"
	s+="<td>"+str(row[1])+"</td>"
	s+="<td>"+str(row[2])+"</td>"
	s+="<td>"+str(row[3])+"</td>"
	s+="<td>"+str(row[4])+"</td>"
	s+="</tr>"
s+="</table>"	

print("<p> %s </p>" % (s,))   
conn.close()
print("""<a href="http://localhost/login.html" id="za"> Click me </a>""")
print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

print("</body>")
print("</html>")