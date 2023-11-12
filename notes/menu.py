import open_notes
import add_note
import change_note
import delete_note
import view_notes


def choosing_action():
    print('Меню:\n')
    menu_item = input(
        ' Показать все заметки - 1\n Показать заметки за день- 2\n Новая заметка - 3\n'
        ' Изменить заметку - 4\n Удалить заметку - 5\n')
    try:
        menu_item = int(menu_item)
    except Exception:
        print('Ни один пункт меню не выбран.')
    print()

    return menu_item


def main_menu_start():
    new_notes = open_notes.read_notes_file()
    a = input('Для доступа в меню введите "*"\n')
    while a == '*':
        choice = choosing_action()
        if choice == 1:  # посмотреть все заметки
            view_notes.all_notes_view(new_notes)
            print()
        elif choice == 2:  # посмотреть все заметки за определённую дату
            view_notes.view_sorted_notes(new_notes)
            print()
        elif choice == 3:  # создать новую заметку
            open_notes.rewrite_note(add_note.new_note(new_notes))
            print()
        elif choice == 4:  # изменить существующую заметку
            open_notes.rewrite_note(change_note.change_note(new_notes))
            print()
        elif choice == 5:  # удалить заметку
            open_notes.rewrite_note(delete_note.delete_note_in_notes(new_notes))
            print()
        else:
            a = 0
    else:
        print('Работа с заметками завершена')
