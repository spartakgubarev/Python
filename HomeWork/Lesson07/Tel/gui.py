import db


def info():
    return input('1 - Открыть файл, 2 - Выход: ')


def what_do():
    return input('Что делаем:\n1 - Вывести справочник\n2 - Искать\n3 - Добавить\n4 - Сохранить\n5 - Вернуться\n')


def write_f():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    tel_number = input('Введите телефон в формате (89211234567): ')
    description = input('Введите описание: ')
    return first_name, last_name, tel_number, description


def read_f():
    return input('Что ищем? (введите имя, фамилию, телефон или описание: ')


def f_name():
    return input('Введите имя файла и расширение: ')


def f_print(text):
    text = list(map(lambda x: x.replace('\n', ''), text))
    text = list(map(lambda x: x.replace(';', ' '), text))
    [print(i) for i in text]
