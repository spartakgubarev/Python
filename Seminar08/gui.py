

# what to do?
def what_to_do():
    print('Телефонный справочник. Выберите действие: ')
    value = input('1- добавить, 2 - искать, 3 - изменить, 4 - удалить, 5 - выход: ')
    return value

# data request
def personal_data():
    f_name = input('Введите имя: ')
    l_name = input('Введите фамилию: ')
    birth = input('Введите дату рождения: ')
    tel = input('Введите телефон формат(8-921-123-45-67): ')
    description = input('Введите описание: ')
    return f_name, l_name, birth, tel, description

# find text
def search_value():
    search = input('Введите иское значение:')
    return search


# show search       type list
def print_search(list_data):
    print(f'ИД      Имя     Фамилия     Дата рождения       Телефон     Описание')
    print('\t{0}\t{1}\t{2}\t{3}\t{4}'.format(list_data[0], list_data[1],\
                list_data[2], list_data[3], list_data[4]))