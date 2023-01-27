def read_file():
    path = 'HomeWork/Lesson08/Company/db.csv'
    ls = []
    with open(path, encoding='utf-8') as f:
        return f.readlines()


