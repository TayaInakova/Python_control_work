import datetime
import json
import random


def create_new_note(id):
    note = {"ID": id,
            "Date": datetime.datetime.today().strftime("%d.%m.%Y  %H:%M"),
            "Title": input("Введите заголовок заметки:\n"),
            "Text": input("Введите текст заметки:\n")}
    json.dumps(note, ensure_ascii=False)
    return note


def new_note(notes):
    notes.append(create_new_note(int(random.random()*1000)))
    print("Заметка сохранена!")
    return notes