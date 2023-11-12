def all_notes_view(notes):
    for note in notes:
        print("№", note["ID"], note["Date"], note["Title"])
    note_text_view(notes)


def note_text_view(notes):
    num = input('Введите номер записи для чтения заметки или "0" для выхода из режима чтения заметок: ')
    try:
        number = int(num)
        if number != 0 and number <= len(notes):
            for note in notes:
                if note["ID"] == number:
                    print(note["Text"])
                    break
            note_text_view(notes)
        elif number == 0:
            _ = input('Введите любой символ для возвращения в меню: ')
        else:
            print("нет записи с таким номером")
            note_text_view(notes)
    except Exception:
        print("нет записи с таким номером")


def view_sorted_notes(notes):
    day = input("укажите дату в формате дд.мм.гггг:\n")
    filter_list = []
    for note in notes:
        if day in note['Date']:
            filter_list.append(note)
            print("№", note["ID"], note["Date"], note["Title"])
            print()
    note_text_view(notes)
    return notes