import sys
from stats import word_count, char_count, sort_char_counts

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"Error: {e}"

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 

    book_content = get_book_text(filepath)
    if isinstance(book_content, str):
        print("============ BOOKBOT ============")
        print(f"\nAnalyzing book found at {filepath}...")

        print("\n----------- Word Count ----------")
        total_words = word_count(book_content)
        print(f"Found {total_words} total words")

        print("\n--------- Character Count -------")
        char_counts = char_count(book_content)
        sorted_char_counts = sort_char_counts(char_counts)

        for item in sorted_char_counts:
            print(f"{item['char']}: {item['num']}")

        print("\n============= END ===============")

if __name__ == "__main__":
    main()
