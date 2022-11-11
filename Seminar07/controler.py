import view, math_f, db

def calculation():
    number_1 = view.number_request()
    number_2 = view.number_request()
    operation = view.operation_request()

    db.saving_number(number_1, number_2, operation)
    number = list(map(int, db.reading_number().split(f' {operation} ')))
    result = math_f.equation(operation, number[0], number[1])
    view.output(number[0], number[1], operation, result)
