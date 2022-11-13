
def write_file(data):
    path = 'HomeWork/Lesson07/tel_number.csv'
    with open(path, 'a') as f:
        f.write(f'{data[0]};{data[1]};{data[2]};{data[3]}\n')

def read_file(data):
    pass

def rewrite_file(data):
    pass

