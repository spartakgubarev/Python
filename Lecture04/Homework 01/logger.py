from datetime import datetime as dt
from time import time


def aaa(data):
    time = dt.now().strftime('%H:%M')
    id = data[data.find("id"):data.find(" ")]
    name = data[data.find("name"):data.find("surname")]
    
    with open('G:/Учеба/Разработчик/repo/Python/Lecture04/Homework 01/log.csv', 'a') as file:
        file.write('{};{};{}\n'
                    .format(time, id, name))
