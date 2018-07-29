import re
import os
import string
import random

SPECIAL = '!@#$%&*'

CHARS = string.ascii_letters + string.digits + SPECIAL
RE_STRING = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[" + SPECIAL + "])"


def main(args):
    random.seed = (os.urandom(1024))
    for i in range(args.count):
        print(getPassword(args.length, args.validate, args.chars, args.rule))


def getPassword(length, validate, chars, rule):
    validation_rule = re.compile(rule)
    while True:
        x = ''.join(random.choice(chars) for i in range(length))
        if validate:
            if not validation_rule.search(x):
                continue
        return x


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--length",
        help="set password length (DEFAULT=10)",
        default=10,
        type=int)
    parser.add_argument(
        "-c",
        "--count",
        help="number of passwords to generate (DEFAULT=10)",
        default=10,
        type=int)
    parser.add_argument(
        "-d",
        "--display",
        help="display valid character set and validation rule and exit",
        action="store_true")
    parser.add_argument(
        "-v",
        "--validate",
        help="validate passwords",
        action="store_true")
    parser.add_argument(
        "-ch",
        "--chars",
        help="use the specified character set",
        default=CHARS)
    parser.add_argument(
        "-ra",
        "--remove-ambiguity",
        help="don't use ambiguous characters (1l0O)",
        action="store_true")
    parser.add_argument(
        "-r",
        "--rule",
        help="use the specified (regex) rule to validate passwords",
        default=RE_STRING)

    args = parser.parse_args()

    if(args.remove_ambiguity):
        args.chars = re.sub('[1l0O]', '', args.chars)
    if args.display:
        print(args.chars)
        print(args.rule)
        import sys
        sys.exit()

    main(args)
