def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def get_num_words(filepath):
    book = get_book_text(filepath)
    word_split = book.split()
    word_count = len(word_split)
    print(f"Found {word_count} total words")

def get_char_count(filepath):
    chars = {}
    book = get_book_text(filepath)
    lower_case = book.lower()
    chars = {}
    for i in lower_case:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    print(chars)

                  
                