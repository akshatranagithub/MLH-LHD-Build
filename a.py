import os
from twilio.rest import Client

account_sid = 'AC2e730975f3aa395167eecefb23bcc6b3'
auth_token = '71f106733a370a3eddb79d65f5f7a4bc'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi, I am your Best friend!",
                     from_='+18124322302',
                     to='+918860959138'
                 )

print(message.sid)