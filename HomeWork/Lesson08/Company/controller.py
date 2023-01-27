import view
import database
import find_pers


def main():
    data = database.read_file()
    while True:
        num = view.show_menu()

        if num == 1:
            find = view.find_peaple()
            [view.info(i) for i in data if find in i]

        elif num == 2:
            find = view.find_position().split()
            for j in find:
                [view.info(i) for i in data if j in i]

        elif num == 3:
            find = list(map(int, (view.find_salary().split())))
            for i in data:
                i = i.replace('\n', '')
                ls = i.split(';')
                if int(ls[3]) >= find[0] and int(ls[3]) <= find[1]:
                    view.info(i)

        elif num == 4:
            personal = view.add_new_personal()
            data.append(personal)
            view.info('Сотрудник добавлен.')

        elif num == 5:
            personal = view.personal().replace(' ', ';')
            data = find_pers.find_personal(personal, data, num)

        elif num == 6:
            personal = view.personal().replace(' ', ';')
            data = find_pers.find_personal(personal, data, num)

        elif num == 7:
            pass
        elif num == 8:
            f_name = view.filename()
            database.save_csv(f_name, data)
        elif num == 9:
            exit()
