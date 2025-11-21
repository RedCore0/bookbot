import sys

from stats import get_book_word_count
from stats import get_book_char_count
from stats import sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    book_words_amount = get_book_word_count(book_text)
    print(f"Found {book_words_amount} total words")
    print("--------- Character Count -------")
    char_count = get_book_char_count(book_text)
    sorted_char_count = sort_char_count(char_count)
    for count in sorted_char_count:
        if count["char"].isalpha():
            print(count["char"]+":", count["num"])
    print("============= END ===============")

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
