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
emailid  = form.getvalue('id')
pwd = form.getvalue('pwd')


conn = sqlite3.connect('customer.db')



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>")
print("<title>Hello - Stats</title>")
print("<style type='text/css'>img{ margin-left: 570px; margin-top: 100px;}</style>")
print("</head>")
print("<body>")

i=0
flag=False
cursor = conn.execute("SELECT PASSWORD from CUSTOMER where EMAILID=?",(emailid,))
for row in cursor:
	if pwd==row[0]:
		flag=True
	i+=1	

if i==0 :
	print("<img  src='https://cdn-images-1.medium.com/max/1600/1*v9BSJbg-nwkz4g2VySImBA.png'><br>")
	print("<h2 style='text-align: center;font-size: 40px'>Invalid User</h2><br>")
	print("<div style='text-align:center'>")
	print("<a href='http://localhost/login.html' style='font-size: 20px'> try again </a>")

else :
	if flag==False:
		print("<img  src='https://cdn-images-1.medium.com/max/1600/1*v9BSJbg-nwkz4g2VySImBA.png'><br>")
		print("<h2 style='text-align: center;font-size: 40px'>login unsuccessful</h2><br>")
		print("<div style='text-align:center'>")
		print("<a href='http://localhost/login.html' style='font-size: 20px'> try again </a>")
	else:
		cursor = conn.execute("SELECT FIRSTNAME from CUSTOMER where EMAILID=?",(emailid,))
		for row in cursor:
			n=str(row[0])

		print("<a href='http://localhost/useroptions.html' id='za' hidden>go</a>")
		print("<script type='text/javascript'>")
		print("sessionStorage.setItem('id','"+emailid+"');sessionStorage.setItem('name','"+n+"');document.getElementById('za').click();")
		print("</script>")

		


conn.close()
# print("""<a href="https://www.google.com" id="za"> Click me </a>""")
# print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

print("</body>")
print("</html>")