import result as rs


def search_values(text, sign):
    find_index = text.find(sign)
    i = find_index
    min_index = 0
    max_index = 0

    while i > 0 and text[i-1] >= '0' and text[i-1] <= '9' or text[i-1] == '.':
        i -= 1
    min_index = i
    i = find_index
    
    while i+1 < len(text)-1 and text[i+1] >= '0' and text[i+1] <= '9' or text[i+1] == '.':
        i += 1
    max_index = i
    
    first_value = float(text[min_index:find_index])
    second_value = float(text[find_index+1:max_index+1])
    res = rs.result(first_value, second_value, sign)
    text = text.replace(text[min_index:max_index+1], str(res))
    return text
