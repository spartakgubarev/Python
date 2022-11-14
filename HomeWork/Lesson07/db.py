import csv, gui

def write_file(data):
    path = 'HomeWork/Lesson07/tel_number.csv'
    with open(path, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def read_file(data):
    path = 'HomeWork/Lesson07/tel_number.csv'
    with open(path, 'r+') as f:
        reader = csv.reader(f)
        for row in reader:
            if data in row:
                print(row)
            
def rewrite_file(data):
    pass
