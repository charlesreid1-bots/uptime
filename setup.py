from setuptools import setup, find_packages
import glob
import os

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from cli import __version__, _program

setup(name=_program,
      version=__version__,
      packages=['cli'],
      test_suite='pytest',
      tests_require=['pytest'],
      description='uptime, a command line tool for checking uptime',
      url='https://github.com/charlesreid1-bots/uptime',
      author='Charles Reid',
      author_email='charles@charlesreid1.com',
      license='MIT',
      entry_points="""
      [console_scripts]
      {program} = cli.command:main
      """.format(program = _program),
      install_requires=required,
      keywords=[],
      zip_safe=False)

