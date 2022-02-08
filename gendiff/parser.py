import argparse
import json
import yaml


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if args.first_file.endswith('.yaml') or args.first_file.endswith('.yml'):
        def f_opener(file_path):
            with open(file_path) as f:
                return yaml.safe_load(f)
    if args.first_file.endswith('.json'):
        def f_opener(file_path):
            return json.load(open(file_path))
    return args.first_file, args.second_file, f_opener
