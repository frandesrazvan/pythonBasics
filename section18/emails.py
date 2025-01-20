import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com') # if 587 doesn't work, try 465, or not any port number
smtp_object.ehlo()
print(smtp_object.ehlo()) # (250, b'smtp.gmail.com at your service, [130.41.145.28]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# smtp_object.starttls() # if port 465 is chosen, can skip this step
# print(smtp_object.starttls()) # smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.

import getpass
password = getpass.getpass('Password please: ')