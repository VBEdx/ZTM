# Import smtplib for the actual sending function
# acts as smpt server
import pathlib
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

# create email object
email = EmailMessage()
email["from"] = 'Vadim Belotcaci'
email["to"] = 'belotvad@hotmail.com'
email["subject"] = 'my fist automated email'
# email.set_content('I am learning zero to mastery python course :).')
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() # king of hello message
    smtp.starttls()
    smtp.login('belotvad@gmail.com', 'blah-blah-x7')
    smtp.send_message(email)
    print('email was sent')

