import os
from slack import WebClient
from slack.errors import SlackApiError
from uptime_config import get_slack_apikey, get_slack_channel


"""
uptime slack

Contains functions for posting slack messages.
"""


def send_slack_message(content):
    # The api key is associated with an app, a bot user, and a workspace
    # App should be installed in the channel or this will fail
    apikey = get_slack_apikey()
    channel = get_slack_channel()
    client = WebClient(token=apikey)

    # See python-slackclient readme
    # https://github.com/slackapi/python-slackclient
    try:
        response = client.chat_postMessage(
            channel = channel,
            text = content
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Error posting slack message: {e.response['error']}")
        raise e

def slack_site_down(url):
    content = f"SITE IS DOWN: {url}"
    send_slack_message(content)

def slack_site_stilldown(url):
    content = f"SITE IS (STILL) DOWN: {url}"
    send_slack_message(content)

def slack_site_back(url):
    content = f"SITE IS OK: {url}"
    send_slack_message(content)
