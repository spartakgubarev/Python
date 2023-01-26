# import gui


def open_file(data):
    text = ''
    path = 'HomeWork/Lesson07/Tel/' + data
    try:
        with open(path, encoding='utf-8') as f:
            # reader = f.readline()
            text = [i for i in f] 
            return text
    except IOError:
        return


    
    # with open(path, 'a+',encoding='utf-8') as f:
    #     reader = f.read()
    #     for i in reader:
    #         text += i
    #     return text

