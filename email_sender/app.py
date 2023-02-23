from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rogonykiplagat@gmail.com'
email_password = 'akptxxrdjgydwuyv'

email_reveiver = 'kajin21763@ukbob.com'

subject = "This is super cool check it out"
body = """
I just sent this from vs code super cool right ahhh
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reveiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reveiver, em.as_string())