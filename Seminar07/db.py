def saving_number(a, b, operation):
    path = 'Seminar07/calc.txt'
    with open(path, 'a') as file:
        file.write(f'{a} {operation} {b}\n')

def reading_number():
    path = 'Seminar07/calc.txt'
    with open(path, 'r') as files:
        return files.readlines()[-1]
