import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file)


def generate_diff(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    sorted_dict_keys_1 = sorted(first_file.keys())
    sorted_dict_keys_2 = sorted(second_file.keys())
    first_file_dict = {}
    second_file_dict = {}
    for item in sorted_dict_keys_1:
        if first_file.get(item) == second_file.get(item):
            first_file_dict[item] = ' '
        else:
            first_file_dict[item] = '-'
    for item in sorted_dict_keys_2:
        if first_file.get(item) != second_file.get(item):
            second_file_dict[item] = '+'
    diff_list_1 = [make_list_of_diff(first_file_dict[item], item, first_file[item])
                   for item in first_file_dict]
    diff_list_2 = [make_list_of_diff(second_file_dict[item], item, second_file[item])
                   for item in second_file_dict]
    return print('\n'.join(diff_list_1 + diff_list_2))


def make_list_of_diff(sign, item, value):
    return '{} {}: {}'.format(sign, item, str(value).lower())


if __name__ == '__main__':
    main()
