from gendiff.scripts.gendiff import generate_diff

def main():
    file1_path = 'gendiff/tests/fixtures/file1.json'
    file2_path = 'gendiff/tests/fixtures/file2.json'
    file_1_file2 = open('gendiff/tests/fixtures/correct_answer_file1_first.json')
    equal_files = open('gendiff/tests/fixtures/correct_answer_equal.json')
    file_2_file1 = open('gendiff/tests/fixtures/correct_answer_file2_first.json')
    assert generate_diff(file1_path, file2_path) == file_1_file2.read()
    assert generate_diff(file1_path, file1_path) == equal_files.read()
    assert generate_diff(file2_path, file1_path) == file_2_file1.read()

if __name__ == '__main__':
    main()