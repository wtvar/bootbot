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
        if char.isalpha():            
            if char.lower() in new_dict:
                new_dict[char.lower()] += 1
            else:
                new_dict[char.lower()] = 1
        else:
            pass
    return new_dict

def dict_transfer(dict):
    
    big_list = []
    for key,value in dict.items():
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = value
        big_list.append(new_dict)
    return big_list

def report_print(path,length,chars):
    print(f"--- Begin report of {path} ---")
    print(f'{length} words found in document')
    print("")
    for item in chars:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")
def sort_on(dict):
    return dict["num"]

def dict_ordered(dict):
    od = collections.OrderedDict(sorted(dict.items()))

def main():
    book_text = get_text(path_to_file)
    length = get_word_count(book_text)
    char_count = get_char_count(book_text)
    #print(char_count)
    #print("..........................")
    """list_of_char_dicts = list(char_count.items())
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    print(list_of_char_dicts)
    report_print(path_to_file,length,list_of_char_dicts)"""
    #report_print(path_to_file,length,char_count)
    converted_dicts = dict_transfer(char_count)
    converted_dicts.sort(reverse=True, key=sort_on)
    #print(converted_dicts)
    report_print(path_to_file,length,converted_dicts)
main()



