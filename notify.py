#! python3
# notify.py - Defines the  notify() function that texts a message
# passed to it as a string.
from twilio.rest import Client


account_sid = 'xxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxx'
my_cell = 'xxxxxxxxxxx'
my_twilio = 'xxxxxxxxxxx'
   

def notify(message):
 	client = Client( account_sid, auth_token)
 	client.messages.create(to=my_cell, from_=my_twilio, body=message)


# just add this to the program you need to be notified once it finishes running
# import Notification
# Notification.notify('The boring task is finished.')   