import search


def procedure(text_string):
    
    for i in text_string:
        if i == '*' or i == '/':
            text_string = search.search_values(text_string, i)
    for i in text_string:
        if i == '+' or i == '-':
            text_string = search.search_values(text_string, i)
    return text_string