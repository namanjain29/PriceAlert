import smtplib
from email.message import EmailMessage

def alert_system(product, link):
    email_id = 'xxxx@29@yahoo.com'
    email_pass = 'xxxxx'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'namanjain2912@gmail.com' # receiver address
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)
