import sys

from stats import get_book_words, get_book_text, get_book_chars, sortlist, printformat

count = len(sys.argv)
if count != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    test_text = get_book_text(sys.argv[1])
    word_chars = get_book_chars(test_text)
    word_count = get_book_words(test_text)
    test = sortlist(word_chars)
    printformat(test, sys.argv[1], word_count)
#word_count = get_book_words(test_text)
#print(f"{word_count} words found in the document")
