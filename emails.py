import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com' #server for gmail
port = 465 #465 secure 587 needs another method

sender = 'chaiwalla2019@gmail.com'
password = input('Enter your password here:')
reciever = 'bijishabhinav@gmail.com'

message = MIMEMultipart('alternative') # Lets some clients that can't render HTML know that there is a plaintext version of it.
message['Subject'] = 'Multipart test'
message['From'] = sender
message['To'] = reciever

text = '''\
Hi,
How are you?
Real Python is amazing for emails!
www.realpython.com
'''

html = '''\
<html>
    <body>
        <p> Hi, <br>
        How are you? <br>
        <a href = "www.realpython.com">Real Python </a> is amazing for emails!
        </p>
    </body>
</html>
'''

part1 = MIMEText(text,'plain')
part2 = MIMEText(html,'html')
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,reciever,message.as_string())
