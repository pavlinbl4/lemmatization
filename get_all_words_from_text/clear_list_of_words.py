from get_all_words_from_text.use_txt_file import read_words_file


def remove_easy_words(input_list:list,easy_words:list):
    cleared_words = []
    for word in input_list:
        if len(word) > 2 and word not in easy_words:
            cleared_words.append(word)
    return cleared_words