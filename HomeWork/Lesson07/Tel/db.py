import gui


def open_file(data):
    text = ''
    path = 'HomeWork/Lesson07/Tel/' + data
    try:
        with open(path, encoding='utf-8') as f:
            text = [i.replace('\n', '') for i in f]
            return text
    except IOError:
        return


def save_file(data):
    if data[0] == data[1]:
        name_save = data[0]
        data = gui.add_text()
    else:
        name_save = gui.save_file()
    path = 'HomeWork/Lesson07/Tel/' + name_save
    with open(path, 'w', encoding='utf-8') as f:
        if name_save[-4:] == '.txt':
            for i in data:
                i = i.replace(';', ' ')
                f.write(i + '\n')
        elif name_save[-4:] == '.csv':
            for i in data:
                i = i.replace(' ', ';')
                f.write(i + '\n')
