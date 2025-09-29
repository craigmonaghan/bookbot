from stats import get_num_words, get_char_count, sorting

def main():
    filepath = "books/frankenstein.txt"
    
    get_num_words(filepath)
    get_char_count(filepath)
    
    word_count = get_num_words(filepath)
    print(f"Found {word_count} total words")
    
    chars = get_char_count(filepath)
    sorted_chars = sorting(chars)
    
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
main()