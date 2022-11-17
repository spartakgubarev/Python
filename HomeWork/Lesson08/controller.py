import gui, db


def main():
    path = gui.file_path() 
    a = True
    while a:
        act = gui.what_to_do()
        # What to do? 1 - write, 2 - find, 3 - delete, 4 - exit
        match act:
            case '1': # write
                data = gui.personal_data()
                db.f_write(path, data)
            case '2': # find
                find = gui.search_value()
                db.f_find(path, find)
            case '3': # delete
                db.f_delete(path)
            case '4': # exit
                a = False
