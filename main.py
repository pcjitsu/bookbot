
def main():
    with open('books/frankenstein.txt') as f:
        file_contents=f.read()
        print(file_contents)
    return file_contents
    
def count(file):
    words = file.split()
    count = len(words)
    print(count)

file_contents = main()

count(file_contents)