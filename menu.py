
from processes.show_all_items import show_all_items
from processes.add_item import add_item
from processes.deletion_items import deletion_items
from processes.show_item import show_item
from processes.change_item import change_item
from processes.search_id import search_id


filename = 'file/file_notes.json'

def menu():
    print('Добро пожаловать! Выберите действие!')
    user_operation = 0
    while(user_operation != 6):
        print('1 - Показать список всех заметок')
        print('2 - Посмотреть заметки')
        print('3 - Добавить заметку')
        print('4 - Изменить заметку')
        print('5 - Удалить заметку')
        print('6 - Выход')
        print('')
        user_operation = int(input())
        print('')
        if user_operation == 1:
            print(show_all_items(filename))

        elif user_operation == 2:
            show_all_items(filename)
            print("Введите ID заметки для просмотра содержимого: ")
            id = input()
            index_array = search_id(filename, id)
            if(index_array > -1):
                print(show_item(filename, index_array))
            else:
                print("Нет такого ID!\n")

        elif user_operation == 3: 
            print("Введите заголовок заметки: ")
            header = input()
            print("Введите тело заметки: ")
            text = input()
            if(add_item(filename, header, text) == True):
                print("Заметка успешно сохранена!\n")
            else:
                print("Ошибка! Попробуйте снова.\n")

        elif user_operation == 4:
            show_all_items(filename)
            print("Введите ID заметки для корректировки содержимого: ")
            id = input()
            index_array = search_id(filename, id)
            if(index_array > -1):
                print(show_item(filename, index_array))
                print("Хотите поменять заголовок? Если да введите 1, если нет введите 2 ")
                value = int(input())
                status_header = False
                if(value == 1):
                    print("\nВведите новый заголовок: ")
                    header = input()
                    status_header = True
                print("Хотите поменять текст? Если да введите 1, если нет введите 2 ")
                value = int(input())
                status_text = False
                if(value == 1):
                    print("\nВведите новый текст: ")
                    text = input()
                    status_text = True
                if(status_header == True or status_text == True):
                    if(change_item(filename, index_array, status_header, header, status_text, text) == True):
                        print("Заметка изменена!\n")              
                    else:
                        print("\nИзменения отменены!")
            else:
                print("Нет такого ID!\n")

        elif user_operation == 5:
            show_all_items(filename)
            print("Введите ID удаляемой заметки: ")
            id = input()
            index_array = search_id(filename, id)
            if(index_array > -1):
                if(deletion_items(filename, index_array) == True):
                    print("Заметка успешно удалена!\n")
            else:
                print("Нет такого ID!\n")



