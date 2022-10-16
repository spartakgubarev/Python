import result as rs


def search_values(text, sign):
    if text[0] == '-':
        find_index = text[1:].find(sign) + 1
        i = find_index
    else:
        find_index = text.find(sign)
        i = find_index
    min_index = 0
    max_index = 0

    while i > 0 and text[i-1] >= '0' and text[i-1] <= '9' or text[i-1] == '.' or text[i-1] == text[0]:
        i -= 1
    min_index = i
    if text[0] == '-':
        i = find_index + 1
    else:
        i = find_index

    while i+1 < len(text)-1 and text[i+1] >= '0' and text[i+1] <= '9' or text[i+1] == '.':
        i += 1
    max_index = i
    
    first_value = float(text[min_index:find_index])
    second_value = float(text[find_index+1:max_index+1])
    res = rs.result(first_value, second_value, sign)

    text = text.replace(text[min_index:max_index+1], str(res), 1)
    return text
