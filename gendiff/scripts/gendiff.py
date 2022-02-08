import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file)


def generate_diff(first_file, second_file, f_opener):
    first_file = f_opener(first_file)
    second_file = f_opener(second_file)
    sorted_dict_keys_1 = sorted(first_file.keys())
    sorted_dict_keys_2 = sorted(second_file.keys())
    file1_dict = {}
    file2_dict = {}
    for item in sorted_dict_keys_1:
        if first_file.get(item) == second_file.get(item):
            file1_dict[item] = ' '
        else:
            file1_dict[item] = '-'
    for item in sorted_dict_keys_2:
        if first_file.get(item) != second_file.get(item):
            file2_dict[item] = '+'
    diff_list_1 = [make_diff_list(file1_dict[item], item, first_file[item])
                   for item in file1_dict]
    diff_list_2 = [make_diff_list(file2_dict[item], item, second_file[item])
                   for item in file2_dict]
    return '\n'.join(['{'] + diff_list_1 + diff_list_2 + ['}'])


def make_diff_list(sign, item, value):
    return '{} {}: {}'.format(sign, item, str(value).lower())


if __name__ == '__main__':
    main()
