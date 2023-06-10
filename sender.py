import argparse
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender, password, server, port, connection, recipient, cc, subject, body, attachment):
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

    if connection == 'ssl':
        server = smtplib.SMTP_SSL(server, port)
    else:
        server = smtplib.SMTP(server, port)
        if connection == 'tls':
            server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient.split(',') + cc.split(','), msg.as_string())
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='mail.conf', help='Path to config file')
    parser.add_argument('--sender', default=None, help='Email sender')
    parser.add_argument('--password', default=None, help='Email password')
    parser.add_argument('--server', default=None, help='Email server')
    parser.add_argument('--port', default=None, type=int, help='Email port')
    parser.add_argument('--connection', default=None, help='Email connection type')
    parser.add_argument('--recipient', default=None, help='Email recipient')
    parser.add_argument('--cc', default=None, help='Email cc')
    parser.add_argument('--subject', default=None, help='Email subject')
    parser.add_argument('--body', default=None, help='Email body')
    parser.add_argument('--attachment', default=None, help='Path to attachment file')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)
    sender = args.sender if args.sender else config.get('email', 'sender')
    password = args.password if args.password else config.get('email', 'password')
    server = args.server if args.server else config.get('email', 'server')
    port = args.port if args.port else config.getint('email', 'port')
    connection = args.connection if args.connection else config.get('email', 'connection')
    recipient = args.recipient if args.recipient else config.get('config', 'recipient')
    cc = args.cc if args.cc else config.get('config', 'cc')
    subject = args.subject if args.subject else config.get('config', 'subject')
    body = args.body if args.body else config.get('config', 'body')
    attachment = args.attachment if args.attachment else config.get('config', 'attachment')

    send_email(sender, password, server, port, connection, recipient, cc, subject, body, attachment)
