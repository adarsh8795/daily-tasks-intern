import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='res'
msg['From']='hhh'
msg['To']='goyal.shivank790@gmail.com'
msg.set_content("test mail")
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('ashu.tvilashi@gmail.com','qevezwahrwuhbdxx')
server.send_message(msg)
server.quit()