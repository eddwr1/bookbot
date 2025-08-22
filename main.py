from stats import word_count
from stats import char_count
from stats import sorter
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_filepath = sys.argv[1]

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_text = f.read()
    return file_text

""" 
def main():
    book_text = get_book_text(book_filepath)
    print(f"{word_count(book_text)} words found in the document")


def main():
    book_text = get_book_text(book_filepath)
    print(f"{char_count(book_text)} characters found in the document") """

def main():
    book_text = get_book_text(book_filepath)
    
    # Print word count
    total_words = word_count(book_text)
    print(f"Found {total_words} total words")
    
    # Get and sort character counts
    book_dict = char_count(book_text)
    sorted_chars = sorter(book_dict)
    
    # Print character counts in the expected format
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["num"]
        print(f"{char}: {count}")

main()