# uptime bot

This is a tool called uptime.

This tool takes arguments to check the uptime of a given site/domain
each minute, and sends alerts if something is wrong.

This uses the `noreply` and `slacker` command line utilities
to send emails and slack messages, respectively.

## secrets

To set api key secrets, use the uptime config file at:

```
~/.config/uptime/uptime.conf
```

Fill out the sections like so:

```
[gmail]
email = aaaaaaa@aaaaaaa.com
password = bbbbbbbbbbbbbbbb
recipient_name = cccccccccccccccc
recipient_email = ddddddddddd@dddddddd.com

[slack]
token = xxxxxxxxxxxxx
secret = yyyyyyyyyyyyyy
```
