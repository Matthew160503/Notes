import view


def start():

    print('Выберите номер желаемой операции:\n')
    operation = view.choose_operation()

    if operation == 1:
        view.create_note()

    elif operation == 2:
        view.read_notes()
        print('\nЗаметки в файле Notes отсортированы по времени и дате\n')

    elif operation == 3:
        view.change_notes()
    
    elif operation == 4:
        view.del_notes()
    
    elif operation == 5:
        exit
    else:
        print('Введен несуществующий код операции. Попробуйте еще раз\n')
        start()
    