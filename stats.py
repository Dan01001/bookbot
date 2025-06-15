def num_words_instring(booktext):
    num_words = 0
    split_string = booktext.split()
    num_words = len(split_string)
    return num_words

def num_char_indoc(booktext):
    char_dict = {}
    lower_case_text = booktext.lower()

    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict


def sort_on(dict):
    return dict["num"]

def sorted_dicts(dict_to_sort):

    list_of_dicts = []
    dict_two_entries = {}
    

    for key, value in dict_to_sort.items():
        dict_two_entries = {"char": key , "num": value}
        list_of_dicts.append(dict_two_entries)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
    
    



