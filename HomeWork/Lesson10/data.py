def db():
    path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson10/anekdot_anekdot.txt'
    with open(path, encoding='utf-8') as file:
        return [i for i in file]

