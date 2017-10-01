#!/usr/bin/python3

import sys

def miles_to_feet(miles):
    if not miles:
        print('no miles')


def main():
    args = sys.argv[1:]
    print(args)

if __name__ == "__main__":
    main()