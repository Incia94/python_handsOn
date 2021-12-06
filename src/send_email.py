import smtplib
import getpass


smtp_obj = smtplib.SMTP("smtp.gmail.com", 465)
smtp_obj.ehlo()

#smtp_obj.starttls()

email = getpass.getpass("Enter Email ID:")
password = getpass.getpass("Enter Password:")
smtp_obj.login(email, password)

from_address = email
to_address = email
subject = input("Enter Email Subject:")
message_body = input("Enter Email Message")
msg = "Subject:" + subject + '\n' + "Message"+ message_body
smtp_obj.sendmail(from_address, to_address, msg)

smtp_obj.quit()

