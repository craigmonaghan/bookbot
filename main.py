from stats import get_num_words, get_char_count, sorting
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    word_count = get_num_words(filepath)
    print(f"Found {word_count} total words")
    
    chars = get_char_count(filepath)
    sorted_chars = sorting(chars)
    
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

#check if its being run directly and not imported then ran?
if __name__ == "__main__":
    main()