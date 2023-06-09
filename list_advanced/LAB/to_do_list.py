all_notes = []

while True:
    note = input()

    if note == 'End':
        break

    all_notes.append(note)


def split_by_importance(notes):

    sorted_notes = sorted(notes, key=lambda cnote: int(cnote.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_notes]

    return result_sorted_notes


print(split_by_importance(all_notes))
