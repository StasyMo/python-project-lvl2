from gendiff.scripts.gendiff import generate_diff
import json
import yaml


def main():
    def f_opener_yml(file_path):
        with open(file_path) as f:
            return yaml.safe_load(f)

    def f_opener_js(file_path):
        return json.load(open(file_path))

    file1_path_js = 'gendiff/tests/fixtures/file1.json'
    file2_path_js = 'gendiff/tests/fixtures/file2.json'
    file1_path_yml = 'gendiff/tests/fixtures/file1.yml'
    file2_path_yml = 'gendiff/tests/fixtures/file2.yml'
    file_1_file2_js = open('gendiff/tests/fixtures/'
                           'corr_answer_file1_first.json')
    equal_files_js = open('gendiff/tests/fixtures/'
                          'corr_answer_equal.json')
    file_2_file1_js = open('gendiff/tests/fixtures/'
                           'corr_answer_file2_first.json')
    file_1_file2_yml = open('gendiff/tests/fixtures/'
                            'corr_answer_file1_first.yml')
    equal_files_yml = open('gendiff/tests/fixtures/'
                           'corr_answer_equal.yml')
    file_2_file1_yml = open('gendiff/tests/fixtures/'
                            'corr_answer_file2_first.yml')

    assert generate_diff(file1_path_js, file2_path_js, f_opener_js) \
           == file_1_file2_js.read()
    assert generate_diff(file1_path_js, file1_path_js, f_opener_js) \
           == equal_files_js.read()
    assert generate_diff(file2_path_js, file1_path_js, f_opener_js) \
           == file_2_file1_js.read()

    assert generate_diff(file1_path_yml, file2_path_yml, f_opener_yml) \
           == file_1_file2_yml.read()
    assert generate_diff(file1_path_yml, file1_path_yml, f_opener_yml) \
           == equal_files_yml.read()
    assert generate_diff(file2_path_yml, file1_path_yml, f_opener_yml) \
           == file_2_file1_yml.read()


if __name__ == '__main__':
    main()
