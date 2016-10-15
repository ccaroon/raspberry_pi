import smtplib
from email.mime.text import MIMEText

class Email:

    def __init__(self, host, port, creds):
        self.host     = host
        self.port     = port
        self.username = creds['username']
        self.password = creds['password']

        self.server = smtplib.SMTP( self.host, self.port )
        self.server.starttls()
        self.server.login( self.username, self.password )

    def send(self, to, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['To'] = to
        msg['From'] = self.username

        self.server.sendmail( msg['From'], msg['To'], msg.as_string() )

    def __del__(self):
        self.server.quit()
