from stats import get_num_words, get_word_count, result_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${filepath}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(filepath) 
    word_count = get_word_count(filepath)
    report = result_report(word_count)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in report:
        if letter["label"].isalpha():
            print(f"{letter["label"]}: {letter["value"]}")
    

main()



