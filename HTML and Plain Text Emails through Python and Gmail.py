from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
#https://docs.python.org/3/library/smtplib.html

host = "smtp.gmail.com"
port = 587
username = "mubarizkhan546@gmail.com"
password = "onetreeone"
mubeen = "p176107@nu.edu.pk"

try:

    email_conn = smtplib.SMTP(host, port) #calling smtplib's class //we can work w u, permission not granted tho

    email_conn.ehlo() #hello to the email server

    email_conn.starttls() 
    email_conn.login(username,password)

    # email_conn.sendmail(username, mubeen,"<b> Bawa jeee </b> ,<br/> Mubariz khan from vs code ")
    # # email_conn.login(username,password) #to login <-- if you have anything but accepted; its an error
    # email_conn.quit() #To quit the connection
    #The html tags are treated as string here; so we're going to import a library


    the_msg = MIMEMultipart("alternative") #this is a standard way of calling an html message
    the_msg['Subject'] = "Hello jeeee!"
    the_msg['From'] = username
    the_msg['To'] = mubeen
    plain_txt = "Testing 1 2 3"
    html_txt = """\
        <html>
            <head>  
                <title> Sippin on straight clorine! </title>
            </head>
            <body>
                <p> Hey <br>
                Just testing this message. Made by zuck <a href ="http://facebook.com"> ZUCK </a>
                </p>
            </body>
        </html> """


    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')
    
    #Now we want to attach the plain text & html
    the_msg.attach(part_1)
    the_msg.attach(part_2)

    #now lets look at the message before we send it
    # print(the_msg.as_string())


    email_conn.sendmail(username, mubeen,the_msg.as_string())
    email_conn.quit() #To quit the connection

    
except smtplib.SMTPException:
    print ("error sending message!")
