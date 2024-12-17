
def main():
    with open('books/frankenstein.txt') as f:
        file_contents=f.read()
        print(file_contents)
    return file_contents
    
def count(file):
    words = file.split()
    count = len(words)
    print(count)

def char_count(file):
    low_char = file.lower()
    char_dict = {}
    for char in low_char:
        if(char not in char_dict):
            char_dict[char] = 0
        if(char in char_dict):
            char_dict[char] = char_dict[char] + 1
    print(char_dict)




file_contents = main()

count(file_contents)
char_count(file_contents)