import csv

def write_file(data):
    path = 'HomeWork/Lesson07/tel_number.csv'
    with open(path, 'r+') as f:
        last_number = int(f.readlines()[-1][0])
        last_number += 1
        f.write(f'{last_number},{data[0]},{data[1]},{data[2]},{data[3]}\n')

def read_file(data):
    path = 'HomeWork/Lesson07/tel_number.csv'
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if data in row:
                print(row)
            # print(row)
            
def rewrite_file(data):
    pass
