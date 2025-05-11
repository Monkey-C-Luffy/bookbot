from typing import Dict


def count_words(book_text:str)->int:
    word_count = len(book_text.split())
    return word_count

def char_occurences(book_text:str)-> Dict[str,int]:
    char_dict = {}
    for char in book_text:
        char = char.lower()
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sorted_char_occurences(dict:Dict[str,int]):
    sorted_list = []
    for key,value in dict.items():
        tmp_dict = {}
        tmp_dict["char"] = key
        tmp_dict["num"] = value;
        sorted_list.append(tmp_dict);
    sorted_list.sort(reverse=True,key=lambda d : d["num"])
    return sorted_list