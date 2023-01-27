

def read_file():
    path = 'HomeWork/Lesson08/Company/db.csv'
    # ls = []
    with open(path, encoding='utf-8') as f:
        return f.readlines()


def save_csv(name, data):
    path = 'HomeWork/Lesson08/Company/' + name + '.csv'
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(data)
