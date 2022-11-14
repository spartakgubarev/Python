import gui, db


def main():
    a = True
    
    while a:
        # What to do? 1 - write, 2 - find, 3 - rewrite, 4 - delete, 5 - exit
        act = gui.what_to_do()
        match act:
            case '1': # write
                data = gui.personal_data()
                db.f_write(data)
            case '2': # find
                find = gui.search_value()
                db.f_find(find)
            case '3': # rewrite
                pass
            case '4': # delete
                pass
            case '5': # exit
                a = False
