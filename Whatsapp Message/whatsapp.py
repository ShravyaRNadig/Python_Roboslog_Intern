import os
from twilio.rest import Client


client = Client()

from_whatsapp_number='+14155238886'
to_whatsapp_number='whatsapp:' + os.environ['MY_PHONE_NUMBER']

client.messages.create(body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+15005550006'
                        )