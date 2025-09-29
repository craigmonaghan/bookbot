def get_book_text(filepath):
        with open(filepath) as file:
            file_contents = file.read()
        return file_contents

def get_num_words(filepath):
     book = get_book_text(filepath)
     word_split = book.split()
     word_count = len(word_split)
     print(f"Found {word_count} total words")