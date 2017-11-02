"""Usage: main.py -i <file>...
    main.py -i <file> [--name=<name>|--number=<number>|--city=<city>|--country=<country>|--company=<company>]

    Load configuration from json FILE
Arguments:
    FILE        optional input file
Options:
    -h --help
    --name=<name>:The name
    --number=<number>: The number
    --city=<city>: Name of the city
    --country=<country>: Name of the country
    --company=<company>: Name of the company

"""
import json
from docopt import docopt


def main(args):
    #print(args)
    with open(args["<file>"][0]) as file:
        data = json.load(file)

    if args["--name"] is not None:
        data["name"] = args["--name"]
    if args["--number"] is not None:
            data["number"] = args["--number"]
    if args["--city"] is not None:
            data["city"] = args["--city"]
    if args["--country"] is not None:
            data["country"] = args["--country"]
    if args["--company"] is not None:
            data["company"] = args["--company"]

    print(data)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
