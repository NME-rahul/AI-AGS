import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reminder(sender_email, sender_password, recipient_emails, subject, message_body, smtp_server='smtp.gmail.com', smtp_port=587):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            for recipient_email in recipient_emails:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message_body, 'plain'))
                server.sendmail(sender_email, recipient_email, msg.as_string())
    except Exception as e:
        pass

if __name__ == '__main__':
    sender_email = 'rv42088@gmail.com'
    sender_password = 'vbor sakr qakc dqya'
    recipient_emails = ['neelamsethia066@gmail.com', 'bhushit6122@gmail.com', 'harshitmd99@gamil.com', 'rv42088@gmail.com']

    subject = '🚀 Action Required: Project Issue Reminder 🚀'
    message_body = '''Dear Team,

🌟 This is a friendly reminder about the project issues that require your attention. 🌟

🔍 Please take a moment to review and address any pending issues to keep the project on track. 🔍

Thank you for your cooperation! 🙏

Best regards,
Rahul Verma
'''
    send_reminder(sender_email, sender_password, recipient_emails, subject, message_body)
