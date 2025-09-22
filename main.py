from stats import words_count

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
   content = get_book_text("books/frankenstein.txt")
   print(f"{words_count(content)} words found in the document")

main()