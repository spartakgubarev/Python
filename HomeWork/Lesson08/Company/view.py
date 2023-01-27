def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def find_peaple():
    return input('Find? ')

def find_position():
    return input('Введите искомые должности через пробел (Директор Бухгалтер,\
    Заместитель директора): ')

def find_salary():
    return input('Введите промежуток зарплат через пробел (150000 250000): ')

def del_personal():
    return input('Введите имя и фамилию сотрудника через пробел, для удаления: ')


def add_new_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    salary = input('Salary: ')
    return f'{name};{surname};{position};{salary}\n'


def info(message):
    message = message.replace(';', ' ')
    print(message)