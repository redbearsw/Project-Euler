# -*- coding: utf-8 -*-
import smtplib

#from email.mime.multipart import MIMEMultipart

#from email.mime.text import MIMEText


uname = 'sjwelber@gmail.com'
pw = raw_input("Password for %s" % uname)

name = raw_input("Name of recipient: ")
to = raw_input("Email of recipient: ")


subject = "<3"
body = "Hi %s, my script is working :)" % name
message = """
From: %s
To: %s
Subject: testing
%s""" % (uname, to, body)

#msg = MIMEMultipart()
#msg['From'] = uname
#msg['To'] = to
#msg['Subject'] = subject
#msg.attach(MIMEText(body, 'plain'))

#attachment = open("C:/Users/sophia.welber/Documents/Kim/BIE Radio Ad Copy", 'rb')

#msg.attach(attachment)

#attachment.close()
#msg.attach("BIE Radio Ad Copy")

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.connect()
	server.ehlo()
	server.login(uname, pw)
	server.sendmail(uname, to, body)
	server.close()
	print "Success!"
except:
	print 'something went wrong :('


server.quit()
