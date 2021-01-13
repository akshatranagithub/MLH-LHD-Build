import os
from twilio.rest import Client

account_sid = 'x'
auth_token = 'y'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi, I am your Best friend!",
                     from_='+18124322302',
                     to='+918860959138'
                 )

print(message.sid)
