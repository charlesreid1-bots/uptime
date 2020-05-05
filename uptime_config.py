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
apikey
channel
"""


CONFIG = os.path.join(os.path.expanduser('~'), '.config', 'uptime', 'uptime.conf')


def check_config(f):
    """Wrapper function: check the config file exists before loading it."""
    def wrapper(*args, **kwargs):
        if not os.path.exists(CONFIG):
            raise Exception(f"Error: config file {CONFIG} does not exist!")
        return f(*args, **kwargs)
    return wrapper


@check_config
def safe_get(section, varname):
    """Safely get the value of variable varname from [section] in config file"""
    config = configparser.ConfigParser()
    config.read(CONFIG)
    try:
        var = config.get(section, varname)
    except configparser.NoSectionError as e:
        raise Exception(f"Error: missing section [{section}] in {CONFIG}")
    except configparser.NoOptionError as e:
        raise Exception(f"Error: missing variable {varname} from section [{section}] in {CONFIG}")
    else:
        return var


def get_gmail_recipient():
    """Return (name, email) of recipient of gmail email alerts."""
    return (
        safe_get('gmail', 'recipient_name'),
        safe_get('gmail', 'recipient_email')
    )


@check_config
def get_gmail_secrets():
    """Return (email, password) credentails used to send emails."""
    return (
        safe_get('gmail', 'email'),
        safe_get('gmail', 'password')
    )


@check_config
def get_slack_apikey():
    """Return the API key (bot user token) used to send Slack messages."""
    return safe_get('slack', 'apikey')


@check_config
def get_slack_channel():
    """Return the name of the Slack channel (including leading #) in which to post messages."""
    channel = safe_get('slack', 'channel')
    if not channel.startswith("#"):
        channel = "#" + channel
    return channel
