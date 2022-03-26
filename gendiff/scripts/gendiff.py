import argparse

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')


if __name__ == '__main__':
    parser.print_help()
