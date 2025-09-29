def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def get_num_words(filepath):
    book = get_book_text(filepath)
    word_split = book.split()
    word_count = len(word_split)
    return word_count

def get_char_count(filepath):
    book = get_book_text(filepath)
    lower_case = book.lower()
    chars = {}
    for i in lower_case:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def sort_on(item):
    return item["num"]

def sorting(chars):
    char_count_list = []
    for ch, count in chars.items():
        char_count_list.append({"char": ch, "num": count})
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list
         