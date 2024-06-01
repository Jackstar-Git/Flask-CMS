import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipients, subject, body):
    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        smtp_server = smtplib.SMTP('mail.gmx.net', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        smtp_server.sendmail(sender_email, recipients, message.as_string())
        smtp_server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
    
if __name__ == "__main__":
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your password: ")
    recipients = input("Enter recipient emails (separated by commas): ").split(',')
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    send_email(sender_email, sender_password, recipients, subject, body)
