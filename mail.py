import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('yogeshlucky37179@gmail.com','Lucky143!')
server.sendmail('yogeshlucky37179@gmail.com','pathivadagayathri2003@gmail.com','This mail is sent from python code')
print("mail sent")