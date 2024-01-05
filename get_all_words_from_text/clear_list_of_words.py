def remove_easy_words(input_list: list, easy_words: list):
    cleared_words_list = []
    for word in input_list:
        if len(word) > 2 and word not in easy_words:
            cleared_words_list.append(word)
    return cleared_words_list
