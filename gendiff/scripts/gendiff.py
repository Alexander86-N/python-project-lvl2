#!/usr/bin/env python

import argparse

def generate_diff():
    parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT', '--format FORMAT', dest='', help='set format of output')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    generate_diff()
