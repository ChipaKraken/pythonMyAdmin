#!/usr/bin/python
import cgi, cgitb
import os
import MySQLdb


form = cgi.FieldStorage()
login = form.getvalue('login')
password = form.getvalue('password')
dbname = form.getvalue('dbname')
html = '''<html>
<head>
	<title>Login Form</title>
	<link rel="stylesheet" href="../style.css" type="text/css">
	<style>
		body {background-image:url('http://www.unsigneddesign.com/Seamless_background_textures/thumbs/seamlesstexture6_1200.jpg');}
	</style>
</head>
<body>
<center>'''
body = '''<br/><br/><br/><br/>
	<form class="form-container">
	<div class="form-title"><h2>Log in</h2></div>
	<div class="form-title">Name</div>
	<input class="form-field" type="text" name="login" /><br />
	<div class="form-title">Password</div>
	<input class="form-field" type="password" name="password" /><br />
	<div class="form-title">DB Name</div>
	<input class="form-field" type="text" name="dbname" /><br />
	<div class="submit-container">
	<input class="submit-button" type="submit" value="Submit" />
	</div>
	</form>
</center>
</body>
</html>''' 
print "Content-type:text/html"
if login != None and password != None and dbname != None:
	db = MySQLdb.connect(host="localhost", user=login, passwd=password,db=dbname)
	print "Set-Cookie: user=%s" % login
	print "Set-Cookie: passwd=%s" % password
	print "Set-Cookie: db=%s" % dbname
	print 'Location: cl.py'
print '\r\n\r\n'
print html
print body
