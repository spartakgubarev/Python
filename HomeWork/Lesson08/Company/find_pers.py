import view


def find_personal(find_txt, data, num):
    f_index = -1
    for i in data:
        if i.find(find_txt) != -1:
            f_index = data.index(i)
    if f_index != -1:
        if num == 5:
            del data[f_index]
            view.info('Сотрудник удален.')
            return data
        elif num == 6:
            view.info('Сотрудник найден, что меняем: ')
            data[f_index] = f'{find_txt};{view.update_personal()}'
            view.info('Сотрудник изменен. ')
            return data
    else:
        view.info('Такого сотрудника нет.')
        return data
