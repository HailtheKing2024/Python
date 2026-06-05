import smtplib, ssl

smtp_server = 'smtp.gmail.com' #server for gmail
port = 465 #465 secure 587 needs another method

sender = 'chaiwalla2019@gmail.com'
password = input('Enter your password here:')
reciever = 'bijishabhinav@gmail.com'
message = '''\
Subject: Hello from python!

This message came from a python program u created! pretty cool right?
'''
context = ssl.create_default_context()

with smtplib.SMTP.SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
