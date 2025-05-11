import sys
from stats import count_words,char_occurences,sorted_char_occurences

def get_book_text(filepath:str)->str:
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def print_report(word_count,sorted_char_occurences):
    print("============ BOOKBOT ============\n",
        "Analyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------\n"
          "Found 75767 total words\n"
          "--------- Character Count -------\n")
    for key_num_dict in sorted_char_occurences:
        char = key_num_dict["char"]
        if not char.isalpha():
            continue
        occurences = key_num_dict["num"]
        print(f"{char}: {occurences}")
    print("============= END ===============")
    

def main():
    args = sys.argv[1:]
    if len(args)==0:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(args[0])
    word_count = count_words(book_text)
    char_occurences_dict = char_occurences(book_text)
    sorted_char_occurences_dict = sorted_char_occurences(char_occurences_dict)
    print_report(word_count,sorted_char_occurences_dict)
    
if __name__== "__main__":
    main()
