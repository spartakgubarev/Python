import logger as lg


def read_text():
    path = 'G:/Учеба/Разработчик/repo/Python/Lecture04/Homework 01/text_client.txt'
    file = open(path, 'r')
    with file as line:
        for i in line:
            lg.aaa(i)