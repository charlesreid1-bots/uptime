import os, re, sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

"""
Apply Default Values to Jinja Templates
"""


# Where templates live
TEMPLATEDIR = '.'

# Where rendered templates will go
OUTDIR = '.'

# Should existing files be overwritten
OVERWRITE = False

env = Environment(loader=FileSystemLoader('.'))

tfile = 'uptime.service.j2'
rfile = 'uptime.service'

content = env.get_template(tfile).render({
    "uptime_path" : "/home/charles/uptime"
})

# Write to file
if os.path.exists(rfile) and not OVERWRITE:
    raise Exception("Error: file %s already exists!"%(rfile))
else:
    with open(rfile,'w') as f:
        f.write(content)

