def get_book_text(file):

    with open(file) as bk:
        file_contents = bk.read()

    return file_contents

frank = get_book_text("books/frankenstein.txt")

print(frank)
