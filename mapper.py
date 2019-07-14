#!/usr/bin/env python

# Use the sys module
import sys


def main(separator=','):
        for index, line in enumerate(sys.stdin):
                group, number = line.split(",")
                print('%s%s%s' % (group, separator,number))

if __name__ == "__main__":
    main()
