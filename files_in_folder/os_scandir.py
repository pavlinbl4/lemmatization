import os

from files_in_folder.words_from_text_file import WordsInTextFile


def files_in_folder(path_to_folder, extension):
    return [f.path for f in os.scandir(path_to_folder) if f.is_file() and f.path.endswith(f'.{extension}')]


def work_with_list_of_file(texts):
    common_set = set()
    for text in texts:
        words_set_from_file = WordsInTextFile(text).read_txt()
        common_set = common_set.union(words_set_from_file)
    return common_set


class FilesInFolder:
    def __init__(self, path_to_folder, extension):
        self.path_to_folder = path_to_folder
        self.extension = extension

    def files_list(self):
        return [f.path for f in os.scandir(self.path_to_folder) if
                f.is_file() and f.path.endswith(f'.{self.extension}')]


def main():
    files_in_folder_ = FilesInFolder('/Users/evgeniy/Documents/ANKI/TEXTS/old', 'txt').files_list()
    all_words = work_with_list_of_file(files_in_folder_)
    WordsInTextFile('/Users/evgeniy/Documents/ANKI/TEXTS/words_from_all_file.txt', all_words).write_txt()


if __name__ == '__main__':
    main()
