# Import smtplib for the actual sending function
import smtplib
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
COMMASPACE = ', '
# Create the container (outer) email message.
msg['Subject'] = 'Our family reunion'
me ='me@gmail.com'

family = 'you@gmail.com, uncle@gmail.com'
msg['From'] = me
msg['To'] = COMMASPACE.join(family)
msg.preamble = 'Our family reunion'

# Send the email via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.sendmail(me, family, "You are Invited!!")
s.quit()