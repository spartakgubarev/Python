import csv, gui

# write file
def f_write(data):
    path = 'HomeWork/Lesson08/phonebook.csv'
    with open(path, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# find file
def f_find(search):
    path = 'HomeWork/Lesson08/phonebook.csv'
    with open(path, 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            if search in row:
                gui.print_search(row)
        print('Ничего не найдено.')
