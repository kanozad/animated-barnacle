#!/usr/bin/env python3

import re
import os
import string
import random

SEDENTARY = 1.2
LIGHT = 1.375
MODERATE = 1.55
HEAVY = 1.725
EXTREME = 1.9


def main(args, height, weight, activity, sex):
    print(args)
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sex",
        help="sex (m or f; default = m)")
    parser.add_argument(
        "-a",
        "--activity",
        help="activity level (default = MODERATE)")
    parser.add_argument(
        "-q",
        "--height",
        help="height in inches")
    parser.add_argument(
        "-w",
        "--weight",
        help="weight in pounds")
    args = parser.parse_args()
    global LENGTH
    global COUNT
    if args.sex:
        sex = args.sex
    else:
        sex = 'm'
    if args.activity:
        if args.activity == 'SEDENTARY':
            activity = SEDENTARY
        elif args.activity == 'LIGHT':
            activity = LIGHT
        elif args.activity == 'MODERATE':
            activity = MODERATE
        elif args.activity == 'HEAVY':
            activity = HEAVY
        else:
            activity = EXTREME
    else:
        activity = MODERATE
    if not args.height:
        raise "Height is required"
    if not args.weight:
        raise "Weight is required"

    height = int(args.height)
    weight = int(args.weight)

    main(args, height, weight, activity, sex)
