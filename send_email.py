import smtplib

# gmail server configuration
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

# Add credentials and the log in
user = "example@gmail.com"
password = "secret"
smtpserver.login(user, password)

sender = "example@gmail.com"
recepient = "example2@gmail.com"

message = "Add your message here"

smtpserver.sendmail(sender, recepient , message)
smtpserver.quit()
