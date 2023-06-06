import argparse
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender, password, server, port, recipient, cc, subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Cc'] = cc
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        with open(attachment, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' % attachment)
            msg.attach(part)

    server = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)
    server.sendmail(sender, recipient.split(',') + cc.split(','), msg.as_string())
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='mail.conf', help='Path to config file')
    parser.add_argument('--recipient', required=True, help='Email recipient')
    parser.add_argument('--cc', default='', help='Email cc')
    parser.add_argument('--subject', default='', help='Email subject')
    parser.add_argument('--body', required=True, help='Email body')
    parser.add_argument('--attachment', default=None, help='Path to attachment file')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)
    sender = config.get('email', 'sender')
    password = config.get('email', 'password')
    server = config.get('email', 'server')
    port = config.getint('email', 'port')

    send_email(sender, password, server, port, args.recipient, args.cc, args.subject, args.body, args.attachment)
