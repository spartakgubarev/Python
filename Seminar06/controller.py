import procedure as proc


def button_click():
    # text = input('Введите выражение в формате: "5+4-3/2*6-7": ')
    text = '20/1+3/1-5*7-40-3/2-10/1'
    text += "="
    text_string = proc.procedure(text)
    text_string = float(text_string[:-1])
    print (text, text_string)


