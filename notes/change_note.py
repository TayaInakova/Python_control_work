import add_note


def change_note(notes):
    changed = int(
        input('Введите номер записи, которую хотите изменить: '))
    try:
        for note in notes:
            if note["ID"] == changed:
                notes.remove(note)
                notes.append(add_note.create_new_note(changed))
                print("Запись изменена!")
        _ = input('Введите любой символ для возвращения в меню: ')
    except Exception:
        print('Нет записи с таким номером.')
    return notes
