import os, sys
import argparse
from . import _program
from . import __version__


logo = f"""
 _  _  ____  ____  __  _  _  ____
/ )( \(  _ \(_  _)(  )( \/ )(  __)
) \/ ( ) __/  )(   )( / \/ \ ) _)
\____/(__)   (__) (__)\_)(_/(____)

        the one and only
           uptime bot

        Version: {__version__}

"""


def main(sysargs = sys.argv[1:]):

    parser = get_argument_parser(sysargs)

    # Make sure the user provided SOME arguments
    if(len(sys.argv)==1):
        sys.stderr.write(logo)
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse the arguments
    args = parser.parse_args(sysargs)

    work_dir = args.dir

    print("Working directory:")
    print(work_dir)
    print("Searching for directory on disk...")
    if os.path.isdir(work_dir):
        print("Found!")
    else:
        print("Does not exist!")


def get_argument_parser(sysargs):
    """Assemble and return an argument parser object"""

    parser = argparse.ArgumentParser(prog = 'uptime')

    required_args = parser.add_argument_group('Required Arguments')
    required_args.add_argument(
        '-d', 
        '--dir',
        required=True,
        help="""Specify the location on disk of the directory"""
    )

    return parser


if __name__ == '__main__':
    main()
