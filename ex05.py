import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output', help="output contents to a new file", action="store_true")
parser.add_argument('text', nargs= '+', help="first text to be concatenated")
args = parser.parse_args()

total_files = len(args.text) - 1
iterator = 0
for arg in args.text:
    if args.output and iterator == total_files:
        with open(arg, 'w') as file:
            file.write(data)
            
    iterator += 1
    with open(arg) as fp:
        if iterator == 1:
            data = fp.read()
        else:
            data += fp.read()
