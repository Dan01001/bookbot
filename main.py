import sys
from stats import num_words_instring
from stats import num_char_indoc
from stats import sorted_dicts

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    number_of_words = 0
    text = ""
    chars = {}

    book = sys.argv[1]
    text = get_book_text(book)
    
    number_of_words = num_words_instring(text)   
    chars = num_char_indoc(text)      
    sorted = sorted_dicts(chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for item in sorted:
        if(item.get("char").isalpha()):
            print(f"{item.get("char")}: {item.get("num")}")

main()

