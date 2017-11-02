"""Usage: main.py -i <file>...

    Load configuration from json FILE
Arguments:
    FILE        optional input file
Options:
    -h --help
"""
import json
from docopt import docopt


def main(args):

    #print(args["<file>"])
    with open(args["<file>"][0]) as file:
        data = json.load(file)
    print(data)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
