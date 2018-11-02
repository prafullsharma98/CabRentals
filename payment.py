#!"C:\Users\Mahe\Anaconda3\python.exe"
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
carid  = form.getvalue('carids')
name  = form.getvalue('name')
emailid  = form.getvalue('emailid')
fromdate  = form.getvalue('fdate')
todate = form.getvalue('tdate')
days  = form.getvalue('days')
adddress  = form.getvalue('address')
state  = form.getvalue('state')
ptime = form.getvalue('ptime')
dtime = form.getvalue('dtime')


conn = sqlite3.connect('customer.db')

cursor = conn.execute("SELECT PRICEPERDAY FROM CAR WHERE ID=?",(carid,))
for row in cursor:
	price=str(row[0])

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>")
print("<title>payment stats</title>")
print("</head>")
print("<body>")
print("hello")

pay=str(int(price)*int(days))

print("<p> %s </p>" % (pay,))

carid  = str(carid)
name  = str(name)
emailid  = str(emailid)
fromdate  = str(fromdate)
todate = str(todate)
days  = str(days)
adddress  = str(adddress)
state  = str(state)
ptime =str(ptime)
dtime = str(dtime)
pay=str(pay)



print("<p> %s %s %s %s %s %s %s %s %s %s %s</p>" % (name,emailid,carid,fromdate,todate,days,address,state,ptime,dtime,pay))


# conn.execute("INSERT INTO PAYMENT(NAME,EMAILID,CARID,FROMDATE,TODATE,DAYS,ADDRESS,STATE,PICKUPTIME,DROPOFFTIME,PAY) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(name,emailid,carid,fromdate,todate,days,address,state,ptime,dtime,pay))

# conn.commit()

print("<p>rec added</p>")

conn.close()
# print("""<a href="https://www.google.com" id="za"> Click me </a>""")
# print("""<script type="text/javascript"> document.getElementById('za').click() </script>""")

print("</body>")
print("</html>")