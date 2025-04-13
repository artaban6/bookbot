from stats import get_num_of_words, get_num_of_characters, get_dict
import sys


def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    count = get_num_of_words(book_text)
    get_num_of_characters(book_text)
    sorted_dict = get_dict(get_num_of_characters(book_text))
    # print(get_dict(get_num_of_characters(book_text)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"{k}: {v}")
        else:
            pass
    print("============= END ===============")


main()
