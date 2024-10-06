import collections


path_to_file = "books/frankenstein.txt"

def get_text(path):
    with open(path_to_file) as f:
        return f.read()

def get_word_count(text):
      words = str(text).split()
      return len(words)

def get_char_count(text):
    new_dict = {}
    for char in text:
        if char.lower() in new_dict:
            new_dict[char.lower()] += 1
        else:
            new_dict[char.lower()] = 1
    return new_dict

def dict_transfer(dict):
    new_dict = {}
    for key,value in dict.items():
        new_dict["name"] = key
        new_dict["num"] = value
    return new_dict

def report_print(path,length,chars):
    print(f"--- Begin report of {path} ---")
    print(f'{length} words found in document')
    for char,count in chars.items():
        print(f"The '{char}' character was found {count} times")

def sort_on(dict):
    return dict["num"]

def dict_ordered(dict):
    od = collections.OrderedDict(sorted(dict.items()))

def main():
    book_text = get_text(path_to_file)
    length = get_word_count(book_text)
    char_count = get_char_count(book_text)
    #print(char_count)
    """list_of_char_dicts = list(char_count.items())
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    print(list_of_char_dicts)
    report_print(path_to_file,length,list_of_char_dicts)"""
    #report_print(path_to_file,length,char_count)
    print(dict_transfer(char_count))
    
main()



