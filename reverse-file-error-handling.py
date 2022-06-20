import argparse

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the file to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

#parse the arguments
args = parser.parse_args()
#print(args)

#carry out the script - read the file, reverse the contents and print

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
