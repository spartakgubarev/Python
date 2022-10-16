import procedure as proc


def button_click():
    text = input('Введите выражение в формате: "5+5-4/2*5-7/(10-3)": ')
    qqq = text + ' ='
    if '(' in text:
        txt = proc.procedure(text[text.find('(')+1:text.find(')')] + '=')
        text = text.replace(text[text.find('('):text.find(')')+1], str(txt[:-1]), 1)
    
    text += "="
    text_string = proc.procedure(text)
    text_string = float(text_string[:-1])
    print (qqq, text_string)


