#!/usr/bin/python
import cgi, cgitb
import MySQLdb
import os
import time
import sys
import Cookie

form = cgi.FieldStorage()
tmp = ''
query = form.getvalue('q')

if query == 'logout':
	c=Cookie.SimpleCookie()
	c['user']=''
	c['user']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	c['passwd']=''
	c['passwd']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	c['db']=''
	c['db']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
	print c
	print "Content-type:text/html"
	print 'Location: login.py'
print "Content-type:text/html"
try:
	cookie = os.environ['HTTP_COOKIE']
except Exception, e:
	print 'Location: login.py'
print '\r\n\r\n'

userq = ''
passwdq = ''
dbq = ''


try:
	if query != None:
		if 'drop' in query or 'DROP' in query:
			print 'What are you doing... Huh?'
			sys.exit(0)
		if 'delete' in query or 'DELETE' in query:
			print 'What are you doing... Huh?'
			sys.exit(0)
except Exception, e:
	print "Check ERROR"
cookie = cookie.split(';')
for param in cookie:
	if 'user=' in param:
		userq = param[5:]
	if 'passwd=' in param:
		passwdq = param[8:]
	if 'db=' in param:
		dbq = param[4:]
try:
	db = MySQLdb.connect(host="localhost", user=userq, passwd=passwdq,db=dbq)
	cur = db.cursor()
except Exception, e:
	print "DB ERROR"
	print e
print '<a href="http://10.1.1.21/~chyngyz/cgi-bin/cl.py?q=logout">Log out</a>'
print '''<html 
lang="en"><head><meta charset="utf-8" /><title>jQuery UI Autocomplete - Default functionality</title>
		<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" /><script src="http://code.jquery.com/jquery-1.9.1.js"></script>
		<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script><link rel="stylesheet" href="/resources/demos/style.css" />
		<script>$(function(){var availableTags = ['''
print '''];$( "#tags" ).autocomplete({source: availableTags});});</script></head>
<body><center><div class="ui-widget"><form class="form-container"><input type="text" id="tags" name="q"><br>
<input class="submit-button" type=submit value="Submit"></form></div>'''
cur.execute("show tables;")
print '<table border="1">'
for i in cur.fetchall():
	print '<tr>'
	wer = str(i)
	desc = '<a href="?q=desc+%s%%3B">desc</a>' % wer[2:-3]
	showAll = '<a href="?q=select+*+from+%s%%3B">show all</a>' % wer[2:-3]
	more = '<a href="#">more...</a>'
	print '<td>%s</td><td>%s</td><td>%s</td><td>%s</td>' % (wer[2:-3], desc, showAll, more)
	print '</tr>'
print '</table>'
print '</center>'

if ';' in query:
	query = query.split(';')
	query.pop()
try:
	if query != None:
		for zapr in query:
			temp = '%s' % zapr
			cur.execute(temp)
			db.commit()
			print '<table border="1">'
			for i in cur.fetchall():
				print '<tr>'
				tt = '<td>%s</td>' * len(i) 
				print tt % i
				print '</tr>'
			print '</table>'
			print '<br><br>'
except Exception, e:
	print 'ERROR:'
	print e