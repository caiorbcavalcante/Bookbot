from stats import count_words, get_book_text, count_characters, format_output
from collections import Counter
import sys

enter = sys.argv
if len(enter) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = enter[1]
book_text = get_book_text(book_path)
word_count = count_words(book_text)
char_count = count_characters(book_text)
    
format_output("", word_count, char_count)

