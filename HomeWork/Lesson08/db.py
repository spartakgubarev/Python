import csv, gui
from datetime import datetime

# write file
def f_write(path, data):
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        log = f'{datetime.now()} - add: {data}\n'
        loger(log)

# find file
def f_find(path, search):
    with open(path, 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            if search in row:
                gui.print_search(row)

# delete
def f_delete(path):
    f_del = input('Какой телефон удалить: ')
    lines = []
    with open(path, 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not f_del in row:
                lines.append(row)
            elif f_del in row:
                log = f'{datetime.now()} - delete: {row}\n'
                loger(log)

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)


def loger(value):
    path = 'HomeWork/Lesson08/log.txt'
    with open(path, 'a') as file:
        file.writelines(value)
