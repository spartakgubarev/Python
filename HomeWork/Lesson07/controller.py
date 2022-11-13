import gui, db

def main():
    a = True
    while a:
        read_write = gui.read_write() # узнаем у пользоватателя что будем делать с файлом

        if read_write == 2: # если значение 2, записываем файл
            data = gui.write_f()
            db.write_file(data)

        elif read_write == 1: # если значение 1, читаем файл
            data = gui.read_f()
            db.read_file(data)
                        
        elif read_write == 3: # если значение 3, редактируем файл
            pass
        elif read_write == 4: # если значение 4, выход
            a = False
