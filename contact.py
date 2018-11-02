#!"E:\Python3\python.exe"
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3
import json

form = cgi.FieldStorage() 

data = {}

# Get data from fields
email = form.getvalue('email')
query  = form.getvalue('query')
name = form.getvalue('name')


conn = sqlite3.connect('customer.db')

conn.execute("INSERT INTO Query  \
      VALUES (?,?,?)",(email,name,query));

conn.commit()

data['Email'] = email
data['Query'] = query
data['Name'] = name

i=0


with open('data.json') as f:
	datas=json.load(f)		
for key in datas:
	i=i+1
i=1+i	

a_dict={i:data}
datas.update(a_dict)
with open('data.json','w') as f:
	json.dump(datas,f)


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Stats</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s </h2>" % (name))
conn.close()
print("<a href=\"http://localhost/index.html\" id=\"za\"> Click me </a>")
print("<script type=\"text/javascript\"> document.getElementById('za').click() </script>")

print("</body>")
print("</html>")