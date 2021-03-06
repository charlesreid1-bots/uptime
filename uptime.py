import os
import sys
import time
import datetime
import threading
import requests
import argparse

from uptime_utils import verbose_timedelta
from uptime_gmail import (
    gmail_site_down, 
    gmail_site_back,
    gmail_site_stilldown
)
from uptime_slack import (
    slack_site_down,
    slack_site_back,
    slack_site_stilldown
)


"""
uptime

this is a simple uptime monitor
charles reid
may 2020
"""


PROGRAM = 'uptime'
TARGETS = {
    'https://charlesreid1.com',
}
BROKEN = {}


def main():
    t1 = threading.Thread(target = site_up)
    t2 = threading.Thread(target = site_down)
    t1.start()
    t2.start()
    while True:
        time.sleep(1)


def site_status_ok(url):
    pass


def site_status_back(url):
    print(f"Site is back online: {url}")
    del BROKEN[url]
    gmail_site_back(url)
    slack_site_back(url)


def site_status_down(url):
    print(f"Site is down (first notice): {url}")
    BROKEN[url] = datetime.datetime.now()
    gmail_site_down(url)
    slack_site_down(url)


def site_status_stilldown(url):
    delta = datetime.datetime.now() - BROKEN[url]
    how_long = verbose_timedelta(delta)
    print(f"Site is down ({how_long}): {url}")
    gmail_site_stilldown(url, how_long)
    slack_site_stilldown(url, how_long)


def site_up():
    while True:
        for url in list(TARGETS):
            try:
                r = requests.get(url)
                code = r.status_code
                if code<400:
                    if url in BROKEN.keys():
                        site_status_back(url)
                    else:
                        site_status_ok(url)
                else:
                    if url not in BROKEN.keys():
                        site_status_down(url)
            except requests.ConnectionError:
                if url not in BROKEN.keys():
                    site_status_down(url)
        # Sleep 1 min before repeating
        time.sleep(60)


def site_down():
    while True:
        # Sleep 15 min before trying again
        time.sleep(900)
        for url in list(BROKEN):
            try:
                r = requests.get(url)
                code = r.status_code
                if code<400:
                    site_status_back(url)
                else:
                    site_status_stilldown(url)
            except requests.ConnectionError:
                site_status_stilldown(url)


if __name__ == '__main__':
    main()
