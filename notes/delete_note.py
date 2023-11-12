def delete_note_in_notes(notes):
    deleted = int(
        input('Введите номер записи, которую хотите удалить: '))
    try:
        for note in notes:
            if note["ID"] == deleted:
                notes.remove(note)
        print("Запись удалена!")
        _ = input('Введите любой символ для возвращения в меню: ')
    except Exception:
        print('Нет записи с таким номером.')
    return notes
