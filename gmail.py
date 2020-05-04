import smtplib
from config import get_gmail_secrets, get_gmail_recipient


"""
uptime gmail

Contains useful functions for sending emails via gmail.
Use the config file to set gmail email/password and the
name/email of the recipient of the uptime emails.

Example ~/.config/uptime/uptime.conf:

[gmail]
email
password
recipient_name
recipient_email
"""


EMAIL_TEMPLATE = """\
From: %s <%s>
To: %s <%s>
Subject: %s

%s
"""


def send_email(subject, body):
    gmail_user, gmail_password = get_gmail_secrets()

    from_name, from_email = "dorky uptime bot", gmail_user
    to_name, to_email = get_gmail_recipient()

    email_text = EMAIL_TEMPLATE%(from_name, from_email, to_name, to_email, subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_email, to_email, email_text)
        server.close()
    except:
        print('Error sending email.')
        raise


def gmail_site_down(url):
    subject = f"SITE IS DOWN: {url}"
    body = f"Site is down: {url}"
    send_email(subject, body)


def gmail_site_stilldown(url):
    subject = f"SITE IS (STILL) DOWN: {url}"
    body = f"Site is (still) down: {url}"
    send_email(subject, body)


def gmail_site_back(url):
    subject = f"SITE IS OK: {url}"
    body = f"Site is back up: {url}"
    send_email(subject, body)
