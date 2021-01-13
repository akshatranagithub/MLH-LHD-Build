import os
from twilio.rest import Client

account_sid = os.environ('account_sid')
auth_token = os.environ('auth_token')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi, I am your Best friend!",
                     from_='Twilio-number',
                     to='phone-number'
                 )

print(message.sid)
