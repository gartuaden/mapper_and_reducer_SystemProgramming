#!/usr/bin/env python

# import modules
from itertools import groupby
from operator import itemgetter
import sys


def main(separator='\t'):
        data = {}

        for index, line in enumerate(sys.stdin):
                try:
                        group, number = line.split(",")
                        number = float(number)

                        if group in data.keys():
                                data[group] = max(data[group], number)
                        else:
                                data[group] = number
                except ValueError:
                        pass

        for group, number in data.items():
                print("{}       {}".format(group, number))


if __name__ == "__main__":
    main()
