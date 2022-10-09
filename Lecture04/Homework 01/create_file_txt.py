from datetime import datetime as dt
from time import time

def create_file():
    amount = 1000
    time = dt.now().strftime('%D:%H:%M -')
    path = 'G:/Учеба/Разработчик/repo/Python/Lecture04/Homework 01/text_client.txt'
    file = open(path, 'w')

    for i in range(amount):
        file.write(
            f'id{i} name{i} surname{i} birth{i} place_of_work{i} phone_number{i}\n')
    file.close()
