import smtplib


host = "smtp.gmail.com"
port = 587
username = "mubarizkhan546@gmail.com"
password = "onetreeone"
mubeen = "p176107@nu.edu.pk"

email_conn = smtplib.SMTP(host, port) #calling smtplib's class //we can work w u, permission not granted tho
email_conn.ehlo() #hello to the email server
email_conn.starttls() 
email_conn.login(username,password)
email_conn.sendmail(username, mubeen,"Bawa jeee, Mubariz khan from vs code ")
# email_conn.login(username,password) #to login <-- if you have anything but accepted; its an error
email_conn.quit() #To quit the connection

