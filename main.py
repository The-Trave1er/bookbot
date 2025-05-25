from stats import word_count, letter_count, sorted_dict
import sys

book = sys.argv

def get_book_text(file):

    with open(file) as bk:
        file_contents = bk.read()

    return file_contents

if len(book) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_text = get_book_text(book[1])
book_dict = sorted_dict(letter_count(book_text))

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count(book_text)} total words")
print("--------- Character Count -------")
for letter in book_dict:
    if letter["char"].isalpha():
        print(f"{letter["char"]}: {letter["num"]}")
print("============= END ===============")
