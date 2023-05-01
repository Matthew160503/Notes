import controller

import random
from datetime import datetime
import json

def choose_operation():
    operation = int(input('1 - Создание заметки\n2 - Чтение списка заметок(сортировка по дате)\n'+
                          '3 - Редактирование заметки\n4 - удаление заметки\n5 - выход из приложения\n'))
    return operation

str_json = {}
str_json['Notes'] = []
with open('Notes', 'w') as file:
    json.dump(str_json,file,indent=3)

def create_note():
    id  = random.randint(1000,100000)
    title = input('\nВведите заголовок заметки:\n')
    body = input('\nВведите саму заметку:\n')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save = int(input('Заметка готова. Хотите ли Вы сохранить данную заметку? Если хотите сохранить, введите - 1.'+
                     'Если не желаете сохранять, введите, что захотите\n'))
    if save == 1:
        with open('Notes', 'r') as file:
            str_json = file.read()
        data = json.loads(str_json)
        temp_data = {}
        temp_data['Title'] = title
        temp_data['Id'] = id
        temp_data['Body'] = body
        temp_data['Date'] = date
        data['Notes'].append(temp_data)
        with open('Notes', 'w') as file:
            json.dump(data,file,indent=3)
        controller.start()    
    else: 
        controller.start()

def read_notes():
    with open('Notes', 'r') as file:
            str_json = file.read()
    data = json.loads(str_json)
    data['Notes'] = sorted(data['Notes'],
    key=lambda x: datetime.strptime(x['Date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    print(data)
    with open('Notes', 'w') as file:
            json.dump(data,file,indent=3)
    controller.start()
    
def change_notes():
    with open('Notes', 'r') as file:
        str_json = file.read()
    data = json.loads(str_json)
    str = input('\nВведите заголовок заметки, которую хотите редактировать:\n')
    for temp in data['Notes']:
        if temp['Title'] == str:
            print('Такая заметка существует. Введите текст измененной заметки:\n')
            temp['Body'] = input()
            temp['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open('Notes', 'w') as file:
                json.dump(data,file,indent=3)
            print('Текст и время изменены')
            controller.start()
        else:
            continue
    print('Если никаких оповещений не было, зачит, заметки с таким именем не нашлось')
    controller.start()

def del_notes():
    with open('Notes', 'r') as file:
        str_json = file.read()
    data = json.loads(str_json)
    str = input('\nВведите заголовок заметки, которую хотите удалить:\n')
    for temp in data['Notes']:
        if temp['Title'] == str:
            print('Такая заметка существует. Выполняется удаление:\n')
            data['Notes'].remove(temp)
            with open('Notes', 'w') as file:
                json.dump(data,file,indent=3)
            print('Заметка удалена')
            controller.start()
        else:
            continue
    print('Если никаких оповещений не было, зачит, заметки с таким именем не нашлось')
    controller.start()