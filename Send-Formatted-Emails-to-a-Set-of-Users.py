import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
host = "smtp.gmail.com"
port = 587
username = "mubarizkhan546@gmail.com"
password = ""
class MessageUser:
    user_details = []
    messages = []
    email_details = []
    
    base_message = """
    Hi {name} your purchase was of pkr{total} on the date: {date}
    run it down, let’s run the plane, no
    You know how to kill a vibe
    We in and out on the regular
    this mail was sent to a group of clients; via mubariz khan's python prompt terminal
    -Team SSEO
    """
    
    def add_user(self,name,amount,email):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name[0].upper() + name[1:].lower(),
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today= today)
        detail['date'] = date_text
        if email != None:
            detail["Email"] = email
        self.user_details.append(detail)
        
        
    def get_details(self):
        return self.user_details
    
    
    def make_messages(self):
        
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name = name,
                    date = date,
                    total = amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg    
                    }
                    self.email_details.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    
    def send_email(self):
        
        self.make_messages()
        if len(self.email_details) > 0:
            for detail in email_details:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo() 
                    email_conn.starttls() 
                    email_conn.login(username,password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "zama terminal ta soh yaad kary de"
                    the_msg['From'] = username
                    the_msg['To'] = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(username, [user_email],the_msg.as_string())
                    email_conn.quit()                                    
                except smtplib.SMTPException:
                    print ("error sending message!")
            return True
        return False

        
obj = MessageUser()
obj.add_user("Mubeen", 2345, "p176107@nu.edu.pk")
obj.add_user("Mubasher Mfused", 400, "p180143@nu.edu.pk")
obj.get_details()
obj.send_email()
