#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip
import re

phoneRegex = re.compile(r'''(\+\d{3}|\+\d{3}\s|\d)?
	                         (\d{9}|\d{3}\s\d{6})''',re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # username
     @                    # @ symbol
    [a-zA-Z0-9.-]+        # domain name
    (\.[a-zA-Z]{2,4})     # dot-something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	groups = list(groups)
	groups = "".join(groups)
	matches.append(groups)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print("Copied to clipboard")
	print('\n'.join(matches))
else:
	print("no phone numbers or email addresses found")