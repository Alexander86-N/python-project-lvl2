#!/usr/bin/env python

import argparse
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open('/home/golem86/example/one/two/file1.json'))
    file2 = json.load(open('/home/golem86/example/file2.json'))
    result = element_research(file1, file2)
    return '\n'.join(result)


def element_research(file_one, file_two):
    result = ['{']
    res = []
    list_one, list_two = [_ for _ in file_one.items()], [_ for _ in file_two.items()]
    res.extend(list_one)
    res.extend([_ for _ in list_two if _ not in list_one])
    for item in sorted(res):
        if item not in list_two:
            result.append(convert_to_string(item, '-'))
        elif item not in list_one:
            result.append(convert_to_string(item, '+'))
        else:
            result.append(convert_to_string(item, ' '))
    result.append('}')
    return result


def convert_to_string(items, symbol, indent=' '):
    item1, item2 = items
    key = symbol + indent + item1.rstrip('"') if isinstance(item1, str) else f'{symbol}{indent}{item1}'
    value = item2.rstrip('"') if isinstance(item2, str) else\
            str(item2).lower() if isinstance(item2, bool) else item2
    return f'{indent * 2}{key}: {value}'
        
 
def main():
    parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT', '--format FORMAT', dest='', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
