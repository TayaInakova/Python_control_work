import json
import operator


def read_notes_file():
    with open('notes.txt', 'r', encoding='utf-8') as file:
        f = file.readlines()
        notes = []
        for note in f:
            notes.append(json.loads(note))
        notes.sort(key=operator.itemgetter('Date'))
    return notes


def rewrite_note(notes):
    with open('notes.txt', 'w', encoding='utf-8') as file:
        for note in notes:
            file.write(json.dumps(note, ensure_ascii=False) + "\n")
