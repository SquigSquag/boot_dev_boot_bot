from stats import get_book_text,get_char_count,return_sorted_dict
import sys

def main():
    if len(sys.argv) <=1 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    book_split = book.split()
    charcount = get_char_count(book)
    word_count = len(book_split)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    new_list = return_sorted_dict(charcount)
    for i in new_list:
        print(f"{i["char"]}: {i["num"]}") 
        
    print("============= END ===============")
main()
