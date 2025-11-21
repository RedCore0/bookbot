def get_book_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_book_char_count(book_text):
    lower_cased_text = book_text.lower()
    result = {}
    for char in lower_cased_text:
        if char not in result: result[char] = 0
        result[char]+=1
    return result

def sort_char_count(dict_char_count):
    dictionaries = []
    for char, num in dict_char_count.items():
        dictionaries.append({"char": char, "num": num})
    result = sorted(dictionaries, key=lambda x: x['num'], reverse = True)
    return result
