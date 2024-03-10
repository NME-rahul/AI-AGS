import smtplib
import sys

def send_reminder(senderID, password, emails, issue, fun_break, port=587):
    for i, email in enumerate(emails):
        try:
            server = smtplib.SMTP('smtp.gmail.com', port)
            server.starttls()
            server.login(senderID, password)
            
            server.sendmail(senderID, email, issue)
            server.quit()
        except:
            if fun_break < 15:
                send_reminder(senderID, password, emails[i:], issue, fun_break+1, port=587)

if __name__ == '__main__':
    senderID = 'rv42088@gmail.com'
    password = 'vbor sakr qakc dqya'
    
    emails = ['neelamsethia066@gmail.com', 'bhushit6122@gmail.com', 'harshitmd99@gamil.com', 'rv42088@gmail.com']
  
    issue = '''🚀 Action Required: Project Issue Reminder 🚀
    Dear Team,

    🌟 This is a friendly reminder about the project issues that require your attention. 🌟
    
    🔍 Please take a moment to review and address any pending issues to keep the project on track. 🔍
    
    Thank you for your cooperation! 🙏
    
    Best regards,
    Rahul Verma
    '''
    send_reminder(senderID, password, emails, issue, fun_break=0)
