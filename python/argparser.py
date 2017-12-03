import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
#parser.add_argument("square", help="display a square of a given number", type=int)
#parser.add_argument("echo", help="echo the string you supply")
args = parser.parse_args()
if args.verbose:
    print "verbose turned on"
    verbose = True
#print args.square**2
#print args.echo
