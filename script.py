import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from config import * 

def sendMail(): # IMPORT SAMBA INFO
    if len(sys.argv) > 1:
        print(sys.argv[1])
        print(sys.argv[2])
        print(sys.argv[3])

        if "New session" in sys.argv[1] or "Failed password" in sys.argv[1]:


            # Email configuration
            sender_email = sender
            receiver_email = receiver
            subject = "ALERT"
            body = sys.argv[1] + "\n" + sys.argv[2]

            # Create the MIME message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            # Attach the body to the email
            message.attach(MIMEText(body, "plain"))

            # SMTP server configuration (for Gmail)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = username
            smtp_password = password

            # Create an SMTP session
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                # Start TLS for security
                server.starttls()

                # Login to the email account
                server.login(smtp_username, smtp_password)

                # Send the email
                server.sendmail(sender_email, receiver_email, message.as_string())

            print("Email sent.")
        print('-----------')

if __name__ == "__main__":
    sendMail()