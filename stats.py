def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filepath):
    text = get_book_text(filepath)
    words = text.split()
    return len(words)

def get_word_count(filepath):
    text = get_book_text(filepath)
    word_count = {}
    for letter in text:
        if letter.lower() in word_count:
            word_count[letter.lower()] += 1
        else:
            word_count[letter.lower()] = 1
    return word_count

def sort_on(dict):
    return dict["value"]

def result_report(dictionary):
    dictionaries = [{"label": x, "value": dictionary[x]} for x in dictionary]
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries