import os
import configparser


"""
uptime config

Contains functions for getting variables from the uptime
configuration file. This file should have the following
sections and variables:

[gmail]
email
password
recipient_name
recipient_email

[slack]
token
secret
"""


CONFIG = os.path.join(os.environ['HOME'], '.config', 'uptime', 'uptime.conf')


def check_config(f):
    def wrapper():
        if not os.path.exists(CONFIG):
            raise Exception(f"Error: config file {CONFIG} does not exist!")
        return f()
    return wrapper


@check_config
def get_gmail_recipient():
    config = configparser.ConfigParser()
    config.read(CONFIG)
    try:
        name = config.get('gmail', 'recipient_name')
        email = config.get('gmail', 'recipient_email')
    except configparser.NoSectionError as e:
        # Could fall back to environment variables here
        print(f"Error: missing [gmail] section in {CONFIG}")
        raise e
    except configparser.InterpolationSyntaxError as e:
        print(f"Error: could not parse [gmail] section of {CONFIG}")
        raise e
    else:
        return name, email


@check_config
def get_gmail_secrets():
    config = configparser.ConfigParser()
    config.read(CONFIG)
    try:
        email = config.get('gmail', 'email')
        password = config.get('gmail', 'password')
    except configparser.NoSectionError as e:
        # Could fall back to environment variables here
        raise Exception(f"Error: missing [gmail] section in {CONFIG}")
    else:
        return email, password


@check_config
def get_slack_keys():
    config = configparser.ConfigParser()
    config.read(CONFIG)
    try:
        token = config.get('slack', 'token')
        secret = config.get('slack', 'secret')
    except configparser.NoSectionError as e:
        # Could fall back to environment variables here
        raise Exception(f"Error: missing [slack] section in {CONFIG}")
    else:
        return token, secret
