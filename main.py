from stats import get_word_count, get_character_count, dictionary_to_sorted_list
import sys


def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print("Error: File not found.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = get_word_count(book_text)
        character_count_dictionary = get_character_count(book_text)
        character_count_sorted_list = dictionary_to_sorted_list(
            character_count_dictionary)
        print(f"""============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------""")
        for dict in character_count_sorted_list:
            if dict["char"].isalpha():
                print(f'{dict["char"]}: {dict["num"]}')
        print("============= END ===============")


main()
