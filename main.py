def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    return contents

def num_words_instring(booktext):
    num_words = 0
    split_string = booktext.split()
    num_words = len(split_string)
    return num_words


def main():
    number_of_words = 0
    text = ""

    text = get_book_text("books/frankenstein.txt")
    number_of_words = num_words_instring(text)

    print(f"{number_of_words} words found in the document")



main()

