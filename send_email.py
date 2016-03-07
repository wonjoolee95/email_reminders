'''
Created on Mar 4, 2016

@author: Won_Lee
'''
import smtplib

def send(recipient, subject, body):
    
    assert '@' in recipient


    # Prepare actual message
    message = """\From: {}\nTo: {}\nSubject: {}\n\n{}
    """.format('wonjoolee.testing@gmail.com', recipient, subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('wonjoolee.testing@gmail.com', 'jeromewjlee95')
        server.sendmail('wonjoolee.testing@gmail.com',
            recipient, message)
        server.close()
        print('Email sent successfully')
    except:
        raise AssertionError
    
    
if __name__ == '__main__':
    body = '''\
hey wassup


--------
this email was sent automatically through a program;
for questions and inquiries, please email jeromelee95@gmail.com
'''
    send('jeromelee95@gmail.com', 'herro', body)
    
    
    