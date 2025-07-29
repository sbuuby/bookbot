from stats import word_count, char_counter, dic_sorter
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    book_text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")

    print("--------- Character Count -------")
    char_count = char_counter(book_text)

    print("racism")
    sorted_dic = dic_sorter(char_count)

    for char in sorted_dic:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")
main()