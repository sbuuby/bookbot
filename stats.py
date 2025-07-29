def word_count(file):
    return len(file.split())

def sort_on(items):
    return items["num"]

def char_counter(book_text):
    str_list = list(book_text.lower())
    counted_char = {}
    for char in str_list:
        if char in counted_char:
            counted_char[char] += 1
        else:
            counted_char[char] = 1
    return counted_char

def dic_sorter(dic):
    characters=[]
    for char in dic:
        characters.append({"name": char, "num": dic[char]})
    characters.sort(reverse=True, key = sort_on)
    return characters

