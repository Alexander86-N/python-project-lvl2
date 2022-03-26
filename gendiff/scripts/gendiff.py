#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f FORMAT', '--format FORMAT', dest='', help='set format of output')


def print_h():
    return parser.print_help()


if __name__ == '__main__':
    print_h()
