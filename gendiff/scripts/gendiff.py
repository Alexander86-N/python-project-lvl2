#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')

def print_h():
    return parser.print_help()


if __name__ == '__main__':
    print_h()
