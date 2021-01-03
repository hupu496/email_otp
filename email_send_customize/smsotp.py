import random
import os
from twilio.rest import Client

send_link=input('enter the link:')
phone=input('enter the no:')

#otp= random.randint(100000,999999)
#print(otp)


account_sid = 'AC3532bb388b7080542999e499ee54616a'
auth_token = 'b2473e2e44676fdae7e63e627e170bbb'
client = Client(account_sid, auth_token)

message = client.messages .create(
                     body='your google account remove,please verify the account visit the link:'+str(send_link),
                     from_='+19093253842',
                     to=phone
                 )

print(message.sid)