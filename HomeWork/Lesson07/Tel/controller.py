import gui
import db


def main():
    while True:
        info = gui.info()  # проверяем файл
        if info == '1':
            name_file = gui.f_name()
            data = db.open_file(name_file)
            if data:
                action(data)
            else:
                print(
                    "Файл не существует!\nСоздать новый? (1 - да, любое другое значение - нет):")
                a = input()
                if a == '1':
                    db.save_file([name_file, name_file])
        elif info == '2':
            exit()


def action(txt):
    while True:
        act = gui.what_do()
        if act == '1':  # Вывести справочник
            gui.f_print(txt)
        elif act == '2':  # Искать
            gui.search_text(txt)
        elif act == '3':  # Добавить
            new_user = gui.add_text()
            txt += new_user
        elif act == '4':  # Сохранить
            db.save_file(txt)
        elif act == '5':  # Вернуть на шаг назад
            return
