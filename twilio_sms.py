from twilio.rest import Client

from credentials import account_sid, auth_token, my_cell, my_twilio
# I previously made a file credentials.py with those details I am importing here
# Find these values at https://twilio.com/user/account


client = Client( account_sid, auth_token)
my_message = "Add your desired message here "

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_message)
