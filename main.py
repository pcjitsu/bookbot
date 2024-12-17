
def main():
    with open('books/frankenstein.txt') as f:
        file_contents=f.read()
    return file_contents
    
def count(file):
    words = file.split()
    word_count = len(words)
    return word_count

def char_count(file):
    low_char = file.lower()
    char_dict = {}
    for char in low_char:
        if(char not in char_dict):
            char_dict[char] = 0
        if(char in char_dict):
            char_dict[char] = char_dict[char] + 1
    return char_dict

def print_report(file):
    print('--- Begin report of books/frankenstein.txt ---\n')
    word_count = count(file)
    char_counts = char_count(file)
    print(f'{word_count} words found in the document\n')
    for key in sorted(char_counts):
        print(f'The \'{key}\' character was found {char_counts[key]} times')
    print('--- End report ---')






file_contents = main()

print_report(file_contents)